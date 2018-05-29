#coding:utf-8
import logging
import random
# 正则模块
import re
#import TornadoProject.constants
from TornadoProject import constants
from BaseHandler import BaseHandler
from TornadoProject.utils.captcha.captcha import captcha
from TornadoProject.utils.response_code import RET
from TornadoProject.libs.yuntongxun.CCP import ccp


class ImageCodeHandler(BaseHandler):
    """"""
    def get(self):
        code_id = self.get_argument("codeid")
        pre_code_id = self.get_argument("pcodeid")
        if pre_code_id:
            try:
                # 删除之前的验证码
                self.redis.delete("image_code_%s"%pre_code_id)
            except Exception as e:
                logging.error(e)
        # name 图片验证码名称
        # text 图片验证码文本
        # image 图片验证码二进制数据
        name,text,image = captcha.generate_captcha()
        try:
            # redis设置值，并且可以设置有限时间
            # 并且给redis存放设置一个前缀
            self.redis.setex("image_code_%s"% code_id, constants.PIC_CODE_EXPIRES_SECONDS, text)
        except Exception as e:
            logging.error(e)
            self.write("")
        # 界面返回的是乱码，都是二进制的，所以需要content-Type
        self.set_header("Content-Type","image/jpg")
        self.write(image)
        #self.write('{"ret":1,"start":-1,"end":-1,"country":"\u4e2d\u56fd","province":"\u5e7f\u4e1c","city":"\u5e7f\u5dde","district":"","isp":"","type":"","desc":""}')

class PhoneCodeHandler(BaseHandler):
    """"""
    def post(self):
        # 获取参数
        # 判断图片验证码
        # 若成功
        # 发送短信
        # 不成功：
        #返回错误信息
        mobile = self.json_args.get("mobile")
        image_code_id = self.json_args.get("image_code_id")
        image_code_text = self.json_args.get("image_code_text")
        # all 是传递的参数每一个进行迭代，如果为真才会继续往下执行
        # 如果有一个为假 就不执行
        if not all((mobile,image_code_id,image_code_text)):
            return self.write(dict(errno=RET.PARAMERR,errmsg="参数不完整"))
        # 判断是不是手机号
        if not re.match(r"1\d{10}",mobile):
            return self.write(dict(errno=RET.PARAMERR,errmsg="手机号错误"))

        #判断图片验证码
        try:
            real_image_code_text = self.redis.get("image_code_%s"%image_code_id)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errno=RET.DBERR,errmsg="查询出错"))

        # 数据库不存在此验证码
        if not real_image_code_text:
            return self.write(dict(errno=RET.NODATA,errmsg="验证码已过期"))
        # 进行对比
        if real_image_code_text.lower() != image_code_text.lower():
            return self.write(dict(errno=RET.DATAERR,errmsg="验证码错误"))

        # 验证码成功，生成随机验证码
        # 随机生成4位数，如果前面不够数，补0
        sms_code = "%04d" %random.randint(0,9999)
        try:
            # 存储到redis里面
            self.redis.setex("sms_code_%s"%mobile,constants.SMS_CODE_EXPIRES_SECONDS,sms_code)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errno=RET.DBERR,errmsg="生成短信验证码错误"))

        # 发送短信验证码
        try:
            # 会在控制台返回测试验证码
            # 需要用到异步处理第三方的实现
            # tornado需要进行封装
            # 发送时间单位是 分钟 所以我们设置的300分钟/60 = 5分钟
            ccp.sendTemplateSMS(mobile,[sms_code,constants.SMS_CODE_EXPIRES_SECONDS/60],1)
            # 需要判断返回值 待实现
        except Exception as e:
            logging.error(e)
            return self.write(dict(errno=RET.THIRDERR,errmsg="发送失败"))

        # 成功，直接返回
        self.write(dict(errno=RET.OK,errmsg="OK"))
