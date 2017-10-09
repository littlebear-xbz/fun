#!/usr/bin/python
# encoding: utf-8

import urllib
import urllib2
import re
import time
import os

siteUrl = "http://www.baidu.com"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
# request = urllib2.Request(siteUrl)
Headers = {'User-Agent' : user_agent}
request = urllib2.Request(siteUrl,headers = Headers)
response = urllib2.urlopen(request)
html_site = response.readlines()

for line in html_site:
	print line
	time.sleep(0.05)




