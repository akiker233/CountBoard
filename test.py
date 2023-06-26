# -*- coding: utf-8 -*-

import requests
import json

url = "https://v1.hitokoto.cn/"

response = requests.get(url)

if response.status_code == 200:
    # 解析返回的JSON数据
    data = response.json()

    # 处理JSON数据
    # 例如，打印返回的JSON数据
    print(json.dumps(data, indent=4))
else:
    print("请求失败，状态码：", response.status_code)