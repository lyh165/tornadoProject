# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from CCPRestSDK import REST
import ConfigParser
import logging

# ���ʺ�
# ˵�������˺ţ���¼��ͨ����վ�󣬿��ڡ�����̨��Ӧ���п������������˺� ACOOUNT SID��
_accountSid = '8aaf0708639129c40163a5a60c8f13c5';

# ���ʺ�Token
# ˵�������ʺ�Token����¼��ͨ����վ�󣬿��ڡ�����̨��Ӧ���п������������˺� ACOOUNT TOKEN��
_accountToken = '3b7b9f71c36c4a1bb83ba0729be9ace5';

# Ӧ��Id
# ��ʹ�ù������̨��ҳ��APPID����ֱ�Ӵ���Ӧ�õ�APPID
_appId = '8aaf0708639129c40163a5a60ce813cb';

# �����ַ����ʽ���£�����Ҫдhttp://
#˵���������ַ�������������ó�app.cloopen.com
# ���Ի��� sanboxapp.cloopen.com
# serverIP = 'app.cloopen.com';
_serverIP = 'sanboxapp.cloopen.com';

# ����˿�
#s ˵��������˿ڣ���������Ϊ8883
_serverPort = '8883';

# REST�汾��
# ˵�� REST API�汾�ű��ֲ���
_softVersion = '2013-12-26';



class CCP(object):
    def __init__(self):
        self.rest = REST(_serverIP,_serverPort,_softVersion)
        self.rest.setAccount(_accountSid,_accountToken)
        self.rest.setAppId(_appId)
    # ����ģʽ������ʵ��
    # ����һ������ѣ�ֻ��һ��ȫ��Ψһ��ʵ��
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
    # # ���͵��ֻ�����֤�룬��������Ч
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
#             print "�������"
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

# ***************************** �ٷ�demo *****************************
# # ����ģ�����
# # @param to �ֻ�����
# # @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
# # @param $tempId ģ��Id
#
# def sendTemplateSMS(to, datas, tempId):
#     # ��ʼ��REST SDK
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
# # sendTemplateSMS(�ֻ�����,��������,ģ��Id)