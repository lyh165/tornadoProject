#coding:utf-8
import json
import tornado.web
from tornado.web import RequestHandler,StaticFileHandler
from TornadoProject.utils.session import Session


class BaseHandler(RequestHandler):
    """
    handler基类
    """
    @property
    def db(self):
        """作为RequestHandler对象的db属性"""
        return self.application.db

    @property
    def redis(self):
        """作为RequestHandler对象的redis属性"""
        return self.application.redis

    def prepare(self):
        """预解析json数据"""
        # 界面加载的时候 就触犯xsrf_token
        self.xsrf_token
        #print str("%s : "%(__file__) + str(self.xsrf_token))
        # 添加application/json
        if self.request.headers.get("Content-Type","").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None

    def write_error(self, status_code, **kwargs):
        pass
    def set_default_headers(self):
        self.set_header("Content-Type","application/josn;charset=UTF-8")
    def initialize(self):
        pass
    def on_finish(self):
        pass

    def get_current_user(self):
        """判断用户是否登录"""
        self.session = Session(self)
        return self.session.data

class StaticFileHandler(tornado.web.StaticFileHandler):
    """"""
    def __init__(self,*args,**kwargs):
        """自定义静态文件处理类, 在用户获取html页面的时候设置_xsrf的cookie"""
        super(StaticFileHandler,self).__init__(*args,**kwargs)
        # 静态主页访问就设置xsrf_token
        self.xsrf_token
        print str("%s : "%(__file__) + str(self.xsrf_token))

