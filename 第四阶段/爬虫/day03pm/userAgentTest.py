# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 09:24:22 2018

@author: Administrator
"""

import requests
import random
user_agentList = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60", 
    "Opera/8.0 (Windows NT 5.1; U; en)", 
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]

for _ in range(5):
    headers = {"User-Agent":random.choice(user_agentList)}
    print(headers)
    response = requests.get("http://www.sina.com.cn",headers=headers)
    response.encoding = 'utf-8'
    print(response.status_code) # TODO：思考一下，这里除了根据状态码之外还有没有其他方法
    #来判断访问成功