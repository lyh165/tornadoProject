#coding:utf-8

import uuid
import logging
import json
from TornadoProject import config
# 定义一个session类
# 作用是用来 用户创建的时候 如果没有生成session的时候。给它生成一个session对象

# session = Session(request_handler=self)
# session.session_id = '12adad'
# session.data =


# class Session(object):
#     """"""
#     def __int__(self,request_handler):
#         self.request_handler = request_handler
#         self.session_id = self.request_handler.get_secure_cookie("session_id")
#         if not self.session_id:
#             # 用户第一次访问
#             # 生成一个session_idm全局唯一
#             self.session_id = uuid.uuid4().get_hex()
#             self.data = {}
#         else:
#             # 拿到了 session_id ,去redis中获取数据
#             try:
#                 data = self.redis.get("sess_%s",self.session_id)
#             except Exception as e:
#                 logging.error(e)
#                 self.data = {}
#             if not data:
#                 self.data = {}
#             else:
#                 #序列化 (Serialization)将对象的状态信息转换为可以存储或传输的形式的过程。
#                 # 在序列化期间，对象将其当前状态写入到临时或持久性存储区。
#                 #以后，可以通过从存储区中读取或反序列化对象的状态，重新创建该对象。
#                 # 进行反序列化
#                 self.data = json.load(data)
#
#     # 提供一个save方法 用来保存数据
#     def save(self):
#         #先序列化(对象的状态信息转换为可以存储或传输的形式的过程)
#         json_data = json.dumps(self.data)
#         try:
#             # 将数据保存到redis里面
#             self.redis.setex("sess_%s"%self.session_id,config.session_expires,json_data)
#         except Exception as e:
#             logging.error(e)
#             raise Exception("save session failed")
#         else:
#             self.request_handler.set_secure_cookie("session_id",self.session_id)
#
#     # 清理操作
#     def clear(self):
#         self.request_handler.clear_cookie("session_id")
#         try:
#             self.redis.delete("sess_%s"% self.session_id)
#         except Exception as e:
#             logging.error(e)
#             pass


class Session(object):
    """"""
    def __init__(self, request_handler_obj):

        # 先判断用户是否已经有了session_id
        self._request_handler = request_handler_obj
        self.session_id = request_handler_obj.get_secure_cookie("session_id")

        # 如果不存在session_id,生成session_id
        if not self.session_id:
            self.session_id = uuid.uuid4().hex
            self.data = {}
            request_handler_obj.set_secure_cookie("session_id", self.session_id)

        # 如果存在session_id, 去redis中取出data
        else:
            try:
                json_data = request_handler_obj.redis.get("sess_%s" % self.session_id)
            except Exception as e:
                logging.error(e)
                raise e
            if not json_data:
                self.data = {}
            else:
                self.data = json.loads(json_data)

    def save(self):
        json_data = json.dumps(self.data)
        try:
            self._request_handler.redis.setex("sess_%s" % self.session_id,
                                             config.session_expires, json_data)
        except Exception as e:
            logging.error(e)
            raise e

    def clear(self):
        try:
            self._request_handler.redis.delete("sess_%s" % self.session_id)
        except Exception as e:
            logging.error(e)
        self._request_handler.clear_cookie("session_id")


