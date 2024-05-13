import json,hashlib,time,reply
from dic_search import dic_search
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

#知乎词典搜索函数
def cnki_search(search_input_raw):
    search_input = "".join(search_input_raw.split())
    #输入搜索内容——获取网页数据
    url = 'https://cidian.cnki.net/result/data?stype=list&sysid=112&resid=8'

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '320',
        'Content-Type': 'application/json',
        'Cookie': 'Ecp_ClientId=1220627082500314472; Ecp_ClientIp=125.35.84.190; SID=065117; Ecp_IpLoginFail=220811125.35.84.190; _pk_ref=["","",1660183517,"https://cidian.cnki.net/"]; _pk_id=b91488a8-5772-479a-80e2-2f0548d9a130.1656289515.2.1660183517.1660183517.; _pk_ses=*; language=chs; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"18811269935","ShowName":"18811269935","UserType":"jf","BUserName":"","BShowName":"","BUserType":"","r":"sbFvY9"}; LID=WEEvREcwSlJHSldTTEYyRkZSRjBCWkpWV0trL08zMVgrQWExWk1EOVo3MD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; Ecp_loginuserjf=18811269935; Ecp_notFirstLogin=sbFvY9; c_m_LinID=LinID=WEEvREcwSlJHSldTTEYyRkZSRjBCWkpWV0trL08zMVgrQWExWk1EOVo3MD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=08/11/2022 10:25:52; c_m_expire=2022-08-11 10:25:52; Ecp_session=1; JSESSIONID=B11FEA0526BB83A5EA6572BC43B4B701; idenId=WEEvREcwSlJHSldTTEYyRkZSRjBCWkpWV0trL08zMVgrQWExWk1EOVo3MD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; userName=18811269935; instShowName=; instUserName=; personUserName=18811269935',
        'Host': 'cidian.cnki.net',
        'Origin': 'https://cidian.cnki.net',
        'Referer': 'https://cidian.cnki.net/result?sysid=112&s=vs1&f=vs1&v=%25E8%2581%2594%25E9%2594%2581',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
    }
    # payloadData数据
    payloadData = {
        "sysId": "112",
        "tableId": "498,499,500,501,503,504,563,502",
        "resourceId": "8",
        "start": 0,
        "length": 10,
        "order": {
            "key": "num_char_h",
            "sort": "ASC",
            "dupKey": "sequence",
            "dupSort": "ASC"
        },
        "filter": {},
        "crossDB": {},
        "group": {},
        "searchQuery": [
            {
                "logic": "or",
                "item": [
                    {
                        "key": "vs1",
                        "value": search_input,
                        "logic": "or"
                    }
                ]
            }
        ],
        "extType": 0,
        "fields": ""
    }
    response = requests.post(url, data=json.dumps(payloadData), headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    #输出搜索结果
    result = []
    soup = BeautifulSoup(html, 'html.parser')  # 初始化BeautifulSoup库,并设置解析器
    for div in soup.find_all(name='div'):  # 遍历父节点
        for p in div.find_all(lambda tag: tag.name == 'p' or tag.name == 'b'):  # 遍历子节点 加不加来源and tag.get('class') == ['interpret']
            if p.string is None:
                pass
            else:
                result.append(p.string)
                # result.append('\n')            
    if len(result) == 0:
        cnki_search_result ='抱歉，您的检索未匹配到数据~\n您可尝试：\n 1.调整检索词重新检索\n 2.回复“词源提取码”获取本地词库\n3.回复“城市名+地铁线路图（如北京地铁线路图）”查看地铁线路信息 \n4.回复“交通运输地图”在线查看世界交通运输地图\n 5.回复“软件下载”获取海量免费破解软件'
    else:
        cnki_search_result =''.join(result)
    return cnki_search_result