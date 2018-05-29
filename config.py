#coding=utf-8
import os
settings = {
    "static_path":os.path.join(os.path.dirname(__file__),"static"),
    "template_path": os.path.join(os.path.dirname(__file__), "template"),
    "debug":True,
    "cookie_secret":"PFhM9YFBTTWTFaLm26VOzhJ/Pcnx4EDbl3Cb45b7elY=",
    # "xsrf_cookies":False
    "xsrf_cookies":True #开启xsrf_cookies 需要拿到cookie才能测试
}
# mysql
mysql_options = dict(
    host = "127.0.0.1",
    database = "ihome",
    user = "root",
    password = "mysql"
)

# redis
redis_options = dict(
    host="127.0.0.1",
    port=6379
)

log_file = os.path.join(os.path.dirname(__file__),"logs/log")
log_level = "debug"

session_expires = 86400 #session数据有限期，秒

# 密码加密密钥
# passwd_hash_key = "nlgCjaTXQX2jpupQFQLoQo5N4OkEmkeHsHD9+BBx2WQ="
passwd_hash_key = "ihome@$^*"

# 七牛图片的域名
image_url_prefix = "http://lyh.bkt.clouddn.com/"# 七牛图片的域名

"""

终端 实时查看日志信息
tail -f log

  --log-file-max-size              max size of log files before rollover
                                   (default 100000000)                  文件大小
                                   
 --log-file-num-backups           number of log files to keep (default 10) 最多保存几个文件
 
  --log-file-prefix=PATH           Path prefix for log files. Note that if you
                                   are running multiple tornado processes,
                                   log_file_prefix must be different for each
                                   of them (e.g. include the port number)
                                   保持的文件路径 
  --log-rotate-when                specify the type of TimedRotatingFileHandler
                                   interval other options:('S', 'M', 'H', 'D',
                                   'W0'-'W6') (default midnight)
                                    按照时间创建日志文件
"""