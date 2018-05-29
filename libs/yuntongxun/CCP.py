# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from CCPRestSDK import REST
import ConfigParser
import logging

# 主帐号
# 说明：主账号，登录云通信网站后，可在“控制台”应用中看到开发者主账号 ACOOUNT SID。
_accountSid = '8aaf0708639129c40163a5a60c8f13c5';

# 主帐号Token
# 说明：主帐号Token，登录云通信网站后，可在“控制台”应用中看到开发者主账号 ACOOUNT TOKEN。
_accountToken = '3b7b9f71c36c4a1bb83ba0729be9ace5';

# 应用Id
# 请使用管理控制台首页的APPID或者直接创建应用的APPID
_appId = '8aaf0708639129c40163a5a60ce813cb';

# 请求地址，格式如下，不需要写http://
#说明：请求地址，生产环境配置成app.cloopen.com
# 测试环境 sanboxapp.cloopen.com
# serverIP = 'app.cloopen.com';
_serverIP = 'sanboxapp.cloopen.com';

# 请求端口
#s 说明：请求端口，生产环境为8883
_serverPort = '8883';

# REST版本号
# 说明 REST API版本号保持不变
_softVersion = '2013-12-26';



class CCP(object):
    def __init__(self):
        self.rest = REST(_serverIP,_serverPort,_softVersion)
        self.rest.setAccount(_accountSid,_accountToken)
        self.rest.setAppId(_appId)
    # 单例模式：单个实例
    # 对于一个类而已，只有一个全局唯一的实例
    @classmethod
    def instance(cls):
        if not hasattr(cls,"_instance"):
            cls._instance = cls()
        return cls._instance

    def sendTemplateSMS(self,to,datas,tempId):
        return self.rest.sendTemplateSMS(to,datas,tempId)

ccp = CCP.instance()

if __name__ == "__main__":
    ccp = CCP.instance()
    # cpp = Cpp.instance()
    # # 发送的手机，验证码，几分钟有效
    #ccp.sendTemplateSMS('13246301428',['1234',5],1)



# class CCP(object):
#
#     def __init__(self):
#         self.rest = REST(_serverIP, _serverPort, _softVersion)
#         self.rest.setAccount(_accountSid, _accountToken)
#         self.rest.setAppId(_appId)
#
#     @staticmethod
#     def instance():
#         if not hasattr(CCP, "_instance"):
#             CCP._instance = CCP()
#         return CCP._instance
#
#     def sendTemplateSMS(self, to, datas, tempId):
#         try:
#             result = self.rest.sendTemplateSMS(to, datas, tempId)
#         except Exception as e:
#             print "这里出错"
#             logging.error(e)
#             raise e
#
#         # print result
#         # for k, v in result.iteritems():
#         #     if k == 'templateSMS':
#         #         for k, s in v.iteritems():
#         #             print '%s:%s' % (k, s)
#         #     else:
#         #         print '%s:%s' % (k, v)
#         if result.get("statusCode") == "000000":
#             return True
#         else:
#             return False
#
# ccp = CCP.instance()
#
# if __name__ == "__main__":
#     ccp = CCP.instance()
#     ccp.sendTemplateSMS("13246301428", ["1112", 5], 1)

# ***************************** 官方demo *****************************
# # 发送模板短信
# # @param to 手机号码
# # @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
# # @param $tempId 模板Id
#
# def sendTemplateSMS(to, datas, tempId):
#     # 初始化REST SDK
#     rest = REST(serverIP, serverPort, softVersion)
#     rest.setAccount(accountSid, accountToken)
#     rest.setAppId(appId)
#
#     result = rest.sendTemplateSMS(to, datas, tempId)
#     for k, v in result.iteritems():
#
#         if k == 'templateSMS':
#             for k, s in v.iteritems():
#                 print '%s:%s' % (k, s)
#         else:
#             print '%s:%s' % (k, v)
#
# # sendTemplateSMS(手机号码,内容数据,模板Id)