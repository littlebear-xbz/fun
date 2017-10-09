#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import imghdr
import os

url = 'http://100.11.44.238:8088/Images3/2017/04/26/18/420115006110440989/18542407601.jpg'
url2 = 'http://100.11.44.239:8088/Images2/2017/04/27/18/151012025526058200/18045030501.jpg'
i = 1
s = 'AMX125'
try:
	response = urllib2.urlopen(url,timeout = 1) #timeout 
	webpage = response.read()
	print imghdr.what('',webpage)
	urllib.urlretrieve(url,u'images/%s/%d.jpg'%(s,i))
	print "image saved"
except Exception as e:
	print 'timeout',e
else:
	print "else"
finally:
	print 'end'


