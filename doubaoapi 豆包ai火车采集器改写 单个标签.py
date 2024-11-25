# -*- coding: utf-8 -*-
#python插件定制联系UP淘小白
import sys,importlib
import urllib
from urllib import parse
from urllib.parse import unquote
from urllib.parse import quote
import json
import os
import requests
import re
import random
import time
import re 

from volcenginesdkarkruntime import Ark

def get_doubao_api(api_key, model, pormpt):
    try:
        client = Ark(api_key=api_key)
        completion = client.chat.completions.create(
            model=model,
            messages = [
                {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
                {"role": "user", "content": pormpt},
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        return e 





# if __name__ == '__main__':
#     api_key='b873a4db-e720-4efa-8162-1e036b64a881d'
#     model="ep-20240624053151-fj4hp"
#     pormpt = '写一篇关于春天的七言绝句'
#     print(get_doubao_api(api_key, model, pormpt))


# 火车头默认格式
if len(sys.argv)!= 5:
    print(len(sys.argv))
    print("命令行参数长度不为5")
    sys.exit()
else:
    LabelCookie = parse.unquote(sys.argv[1])
    LabelUrl = parse.unquote(sys.argv[2])
    #PageType为List,Content,Pages分别代表列表页，内容页，多页http请求处理，Save代表内容处理
    PageType=sys.argv[3]
    SerializerStr = parse.unquote(sys.argv[4])
    if (SerializerStr[0:2] != '''{"'''):
        file_object = open(SerializerStr)
        try:
            SerializerStr = file_object.read()
            SerializerStr = parse.unquote(SerializerStr)
        finally:
            file_object.close()
    LabelArray = json.loads(SerializerStr)

#以下是用户编写代码区域
    if(PageType=="Save"):

        o_content = LabelArray['采集内容'] 
        api_key = LabelArray['api_key'] 
        model = LabelArray['model'] 
        prompt = LabelArray['prompt'] 
        
        result = get_doubao_api(api_key, model, prompt+o_content)
        LabelArray['改写内容'] = result
    else:
        LabelArray['Html']='当前页面的网址为:'+ LabelUrl +"\r\n页面类型为:" + PageType + "\r\nCookies数据为:"+LabelCookie+"\r\n接收到的数据是:" + LabelArray['Html']
#以上是用户编写代码区域
    LabelArray = json.dumps(LabelArray)
    print(LabelArray)

#需要在火车采集器中添加的板块
#采集内容、api_key、model、prompt、改写内容
#api_key、model、prompt 三项设置为生成固定格式的数据-固定字符串
#"采集内容1"将由"prompt1"指令改写成为“改写内容1”
#"采集内容2"将由"prompt2"指令改写成为“改写内容2”


