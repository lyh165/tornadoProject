#coding:utf-8

"""
装饰器：必须会写
面试也会问
装饰器是什么
装饰器是一个函数
是对一个函数的封装，返回一个函数
def require_logined(fun):
    def wrapper(*args,**kwargs):
        pass
    return wrapper
"""

"""
判断用户是否登录的 装饰器
装饰器最主要考虑的问题就是
东西从何而来
"""
import functools
from TornadoProject.utils.response_code import RET
def require_logined(fun):
    # @functools.wraps(fun) 到时候返回的函数名是原先的函数名 不会是wrapper
    @functools.wraps(fun)
    def wrapper(request_handler_obj,*args,**kwargs):
        # 根据get_current_user方法判断，如果返回的不是一个空字典。
        # 证明用户已经登录过，保存了用户的session数据
        if not request_handler_obj.get_current_user():
            fun(request_handler_obj,*args,**kwargs)
        # 返回空字典，代表用户未登陆过，没有保存用户的session
        else:
            #  返回错误信息
            # 方法从哪里来的
             request_handler_obj.write(dict(errno=RET.SESSIONERR,errmsg="用户未登录"))
        print str(__file__) + str(fun.__name__)
    return wrapper


"""
使用装饰器的情况
@require_logined
def get(self)

那么相当于
require_logined(get)

而@require_logined 是返回了结果
inner_new_fun = require_logined(get)
inner_new_fun(self)

这时候的inner_new_fun(self)
相当于
wrapper(request_handler_obj,*args,**kwargs):
inner_new_fun(self)中的self 就是指向了warpper中的request_handler_obj
"""

"""
实例
用来演示：装饰器，并且使用装饰器的时候，到时候返回的函数名是原先的函数名


def d(f):
    def wrapper(*args,**kwargs):
        print "inner"
        f(*args,**kwargs)
    return wrapper
@d
def fa():
    print "fa"

fa()

输出
inner
fa    
可以查看fa的 __name__
fa.__name__ 输出 'wrapper'   
     
"""