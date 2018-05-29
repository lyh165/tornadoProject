#coding:utf-8

import logging
from .BaseHandler import BaseHandler
from TornadoProject.utils.image_storage import storage
from TornadoProject.utils.response_code import RET
from TornadoProject.utils.common import require_logined
from TornadoProject.config import image_url_prefix
class AvatarHander(BaseHandler):
    """头像"""
    @require_logined
    def post(self):
        user_id = self.session.data["user_id"]
        try:
            avatar = self.request.files["avatar"][0]["body"]
        except Exception as e:
            # 参数出错
            logging.error(e)
            return self.write(dict(errno=RET.PARAMERR,errmsg="参数错误"))
        try:
            image_name = storage(avatar)
        except Exception as e:
            logging.error(e)
            return self.write({"errno":RET.THIRDERR,"errmsg":"qiniu error"})
        try:
            self.db.execute("update ih_user_profile set up avatar=%s where up user_id=%s",image_name,user_id)
        except Exception as e:
            logging.error(e)
            return self.write({"errno":RET.DBERR,"errmsg":"upload failed"})
        # 返回图片的url
        image_url = image_url_prefix + image_name
        self.write({"errno":RET.OK,"errmsg":"OK","img_url":image_url})
        #return "返回图片的url"
        #return  image_url
