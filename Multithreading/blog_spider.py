"""
博客园url
"""
import requests

urls = []
for i in range(1, 51):
    ur = f"https://ww.cnblogs.com/#p{i}"
    urls.append(ur)

# print(urls)


def func(url):
    s = requests.get(url)
    print(url, len(s.text))


func(urls[1])
