"""
简易网页采集器.利用 UA 伪装
UA :user agent (请求载体的身份标识)
"""
# UA检测:门户网站检测请求头的载体标识

import requests

while True:
    x = input("输入查询信息:")
    if x == "q":
        break
    if not x:
        continue
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
    }
    url = f"https://www.sogou.com/web?"
    param = {
        "query": x
    }
    response = requests.get(url=url, params=param, headers=header)
    page = response.text
    print(page)
    # with open(f"./{x}.html", "w+", encoding="utf-8") as f:
    #     f.write(page)
