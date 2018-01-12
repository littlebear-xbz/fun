# coding: utf-8
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
data = requests.get("http://www.eshow365.com/zhanhui/html/120062_0.html")

print(data.content)