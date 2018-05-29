#coding:utf-8

from qiniu import Auth,put_data,etag,urlsafe_base64_encode
import qiniu.config

"""
怎么判断用户上传的是不是同一张图片 图片名字判断不了
只能用 hash 散列
因为图片的二进制是不会变。不管你的改名叫a.jpg还是q.jpg
它的二进制都是一样的
"""

#需要填写你的 Access Key 和 Secret Key
# access_key = 'Access_Key'
# secret_key = 'Secret_Key'

# 传智播客的账号
access_key = 'uzc59bVURbUbazey9vrexXKocNKBUN8NuLijk57N'
secret_key = '-9lenw28jU2REojvGkcsEPWk5Nm9V2HIVqb5Nkts'


def storage(image_data):
#做开发，需要考虑到所有的东西，比如用户传过来的是不是图片

    if not image_data:
        return None
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = 'ihome'
    # # 上传到七牛后保存的文件名
    # key = 'my-python-logo.png';
    # 生成上传 Token，可以指定过期时间等
    # token = q.upload_token(bucket_name, key, 3600)
    token = q.upload_token(bucket_name, None, 3600)

# # 要上传文件的本地路径
    # localfile = './sync/bbb.jpg'
    ret, info = put_data(token, None, image_data) #put_data
    print(info)
    # assert ret['key'] == key
    # assert ret['hash'] == etag(localfile)
    # 返回图片的url
    # 图片的url = 七牛的外链（或者是我们服务器的ip） + 七牛给我们生成的key(hash散列)
    return ret["key"]

if __name__ == "__main__":
# 模拟测试
    """
    input() 当做表达式去替代
    1+3
    4
    raw_input() 当做字符串去替代
    1+3
    '1+3'
    """
    # 不能打开中文的文件。。。。
    file_name = raw_input("请输入文件名:")
    file = open(file_name,"rb")
    file_data = file.read()
    #print file_data
    key = storage(file_data)
    print key
    file.close()
"""
exception:None, status_code:200, _ResponseInfo__response:<Response [200]>, 
text_body:{"hash":"FsZaex2wxZqTEctIfTYEtFodhLz7","key":"FsZaex2wxZqTEctIfTYEtFodhLz7"}, req_id:K1AAAE-89Nq76zIV, x_log:body;0s.ph;0s.put.in;0s.put.disk;0s.put.out;1s.put.in;1s.put.disk;1s.ph;PFDS;PFDS:1;body;rs38_6.sel/not found;rs37_12.sel:3/not found;rdb.g/no such key;DBD/404;v4.get:1/Document not found;rs38_6.ins:3;rwro.ins:9;RS:9;rs.put:10;rs-upload.putFile:12;UP:14
FsZaex2wxZqTEctIfTYEtFodhLz7

七牛上传图片 计算出来的结果值
"hash":"FsZaex2wxZqTEctIfTYEtFodhLz7"

"""
# C:/Users/Hasee/Desktop/tornado/errorInfo/1.txt
#
# full_path = os.path.realpath(__file__)
# file_path = '%s/a.txt' % os.path.dirname(full_path)
# def method():
#   with open(file_path) as f:
#     print f.readlines()
