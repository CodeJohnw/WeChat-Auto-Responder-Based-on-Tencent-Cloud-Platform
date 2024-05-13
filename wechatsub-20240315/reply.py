#文件名:reply.py
import requests
import json
import urllib.request
import time
import os
import tempfile

def ReplyText(toUser,fromUser,nowtime,content):
    XmlForm = f"""
        <xml>
            <ToUserName><![CDATA[{toUser}]]></ToUserName>
            <FromUserName><![CDATA[{fromUser}]]></FromUserName>
            <CreateTime>{nowtime}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{content}]]></Content>
        </xml>
        """

    return {
    "isBase64Encoded": False,
    "statusCode": 200,
    "headers": {"Content-Type": "application/xml"},
    "body": XmlForm
    }



access_token = None
saved_time = None

def generate_access_token():
    global access_token, saved_time
    AppID = 'wx23fac1320173121f'#微信公众号开发者ID 测试号：wx0624839cec14a789'
    AppSecret = 'e0e92e6952dd2369bcb8b9d4d747dc52'#微信公众号开发者密码 测试号：2bee3053e3cd23022cc7f7ae25c32d4c'
    gurl = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(AppID, AppSecret)
    r=requests.get(gurl)
    dict_result= (r.json())
    #print(dict_result)
    access_token = dict_result['access_token']
    saved_time = time.time()

def get_access_token():
    global access_token, saved_time
    if access_token is None:
        generate_access_token()
        return access_token
    elapsed_time = time.time() - saved_time
    if elapsed_time > 7200:
        generate_access_token()
    return access_token



        

# def Token_get(): #获取token，微信公众号需设置ip白名单 参考教程：https://cloud.tencent.com/document/product/583/38198 https://cloud.tencent.com/developer/article/1698593
#     # # #判断txt文件储存的 access_token是否有效

#     filename = '/tmp/access_token.txt' #必须要加/tmp/，参考：https://cloud.tencent.com/developer/ask/sof/105994432
#     # Reading the ACCESS_TOKEN value from the file
#     with open(filename, encoding='utf-8') as f:
#         stored_token, stored_time = f.read().strip().split(',')
#         elapsed_time = time.time() - float(stored_time)

#     # Checking if the token is expired
#     if elapsed_time < 7200:
#         access_token = stored_token
#     else:
#         #储存的 access_token无效，则重新获取access——token并存入txt文件
#         AppID = 'wx23fac1320173121f'#微信公众号开发者ID 测试号：wx0624839cec14a789'
#         AppSecret = 'e0e92e6952dd2369bcb8b9d4d747dc52'#微信公众号开发者密码 测试号：2bee3053e3cd23022cc7f7ae25c32d4c'
#         gurl = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(AppID, AppSecret)
#         r=requests.get(gurl)
#         dict_result= (r.json())
#         #print(dict_result)
#         access_token = dict_result['access_token']

#         # #将生成的access_token保存并记录保存时间
#         # filename = '/tmp/access_token.txt'
#         # # Storing the value of ACCESS_TOKEN and the timestamp in the file
#         with open(filename, 'w') as f1:
#             f1.write(f'{access_token},{time.time()}')
#         # # else:
#         # #     access_token = value
#     return access_token




def get_media_ID(mediaName):  ##本地文件上传到临时素材  并获取图片ID
    Gtoken = get_access_token()
    img_url = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token={}&type=image".format(Gtoken)
    path = mediaName #图片需要和文件在同一个目录下
    files = {'p_w_picpath': open(path, 'rb')}
    r = requests.post(img_url, files=files)
    re = json.loads(r.text)
    #print(re)
    return re['media_id']


def ReplyImg(toUser,fromUser,nowtime,media_id):
    
    XmlForm = f"""
        <xml>
        <ToUserName><![CDATA[{toUser}]]></ToUserName>
        <FromUserName><![CDATA[{fromUser}]]></FromUserName>
        <CreateTime>{nowtime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
            <MediaId><![CDATA[{media_id}]]></MediaId>
        </Image>
        </xml>
        """

    return {
    "isBase64Encoded": False,
    "statusCode": 200,
    "headers": {"Content-Type": "application/xml"},
    "body": XmlForm
    }