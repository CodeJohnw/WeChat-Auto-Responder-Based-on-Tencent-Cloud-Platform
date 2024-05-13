
def dic_search(Msgcontent):
    f = open("dict.txt", encoding='utf-8')
    lines = f.readlines()
    res = []
    for line in lines:
        if Msgcontent in line:
            res.append(line)
    f.close()
    # toUser = FromUserName
    # fromUser = ToUserName
    # nowtime = str(int(time.time()))
    # MsgType = xmlData.find('MsgType').text
    res_first10 = res[0:10]#取前10个搜索结果
    resu = ''.join(res_first10)
    return resu