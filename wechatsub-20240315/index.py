#导入第三方库
import requests
from bs4 import BeautifulSoup
import json,hashlib,time,reply
import xml.etree.ElementTree as ET

#导入同文件夹下其他py文件函数
from dic_search import dic_search #导入本地文本库
from cnkisearch import cnki_search #导入字典查询


#用户关注自动回复
def main_handler(event, context):
    print(event['httpMethod'])
    print(context)
    #微信后台验证
    if event['httpMethod'] == 'GET':
        return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "plain/text"},
        "body": event['queryString']['echostr']
        }

#根据用户操作回复内容
    if event['httpMethod'] == 'POST':
        #解析微信消息
        webData = event['body']
        xmlData = ET.fromstring(webData)
        #获取xml具体内容
        MsgType = xmlData.find('MsgType').text
        ToUserName = xmlData.find('ToUserName').text
        FromUserName = xmlData.find('FromUserName').text
        CreateTime = xmlData.find('CreateTime').text

        ##回复信息
        #统一指定回复信息发送人、收信人和时间点
        toUser = FromUserName
        fromUser = ToUserName
        nowtime = str(int(time.time()))
        
        #关注自动回复       
        if MsgType == 'event':
            Msgevent = xmlData.find('Event').text
            if Msgevent == 'subscribe':
                with open('AutoReplyContent.txt','r',encoding='utf-8') as f:
                    content = f.read() 
                return reply.ReplyText(toUser,fromUser,nowtime,content)
            else:
                return 'success'
        #根据发送内容回复
        elif MsgType == 'text':
            #获取发送内容
            MsgId = xmlData.find('MsgId').text
            Msgcontent = xmlData.find('Content').text
            MsgType = xmlData.find('MsgType').text
            
            # #发送二维码
            if Msgcontent == '关注公众号':
                mediaName = 'qrcode.jpg'
                # reply.Token_get()
                media_id = reply.get_media_ID(mediaName)
                return reply.ReplyImg(toUser,fromUser,nowtime,media_id)

            #从本地字典搜索结果
            resu = dic_search(Msgcontent)
            #判断本地字典中搜索出的结果是否为空，若不为空直接输出；否则从cnki字典搜索
            #函数结束
            if len(resu) == 0:
                content = cnki_search(Msgcontent)
            else:
                content = resu.strip('\n')
            return reply.ReplyText(toUser,fromUser,nowtime,content)

        elif MsgType == 'voice':
            #获取发送内容
            Msgtext = xmlData.find('Recognition').text
            Msgcontent = Msgtext[:-1]
            MsgId = xmlData.find('MsgId').text
            MsgType = xmlData.find('MsgType').text

            #从本地字典搜索结果
            resu = dic_search(Msgcontent)
            #判断本地字典中搜索出的结果是否为空，若不为空直接输出；否则从cnki字典搜索
            #函数结束
            if len(resu) == 0:
                content = cnki_search(Msgcontent)
            else:
                content = resu.strip('\n')
            return reply.ReplyText(toUser,fromUser,nowtime,content)

        elif MsgType == 'image': #收到图片返回图片的MediaId
            PicUrl = xmlData.find('PicUrl').text
            MediaId = xmlData.find('MediaId').text
            content = MediaId

            return reply.ReplyText(toUser,fromUser,nowtime,content)






   