#coding:utf-8
# 路由(url)
# handlers 是一个文件夹，如果没有 __init__是不能够给python识别的
# 所以 文件夹必须要有 __init__.py文件
#from handlers import BaseHandler
# from Tornado_project.handlers import Passport
#from handlers import Passport,VerifyCode
import os

from handlers import Passport,VerifyCode
from handlers.BaseHandler import StaticFileHandler
urlss = [
    # [(r"/", BaseHandler.IndexHandler), ],
    #(r"/", Passport.IndexHandler),
    (r"/api/register", Passport.RegisterHandler),
    (r"/api/login", Passport.LoginHandler),
    # (r"/api/logout", Passport.LogoutHandler),
    (r"/api/check_login", Passport.CheckLoginHandler),  # 判断用户是否登录

    (r"/api/imagecode", VerifyCode.ImageCodeHandler),
    (r"/api/smscode", VerifyCode.PhoneCodeHandler),
    (r"/(.*)",StaticFileHandler,dict(path=os.path.join(os.path.dirname(__file__),"html"),default_filename="index.html"))
]
