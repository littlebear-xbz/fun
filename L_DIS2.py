#!/bin/usr/python
#encoding: utf-8

# hphm.txt need encode with utf-8

import os #mkdir
import time
import sys #path
import shutil # rmtree
import cx_Oracle
import imghdr
import urllib
import urllib2

reload(sys)
sys.setdefaultencoding("utf-8") #设置中文文件夹

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

#  url save images
def downloadimage(args):
	pass


# 
def geturl(args):
	pass

def mkimages():
	if os.path.exists('images'):
		shutil.rmtree('images')
		print "rm images"
		time.sleep(1)
		os.mkdir('images')
		print "mkdir images"
	else:
		os.mkdir('images')
		print "mkdir images"

#
def start():
	mkimages()
	cp_in = open('hphm.txt')
	lines = cp_in.readlines()
	print lines
	try:
		db = cx_Oracle.connect('si01','jp2011','100.11.44.237/SICSDB')
		for line in lines:
			hphm = line.strip()
			cphm = line[3:9]
			# print cphm
			path = 'images/%s'%hphm
			#path = unicode(path,"GB2312")# chinese code problem
			if os.path.exists(path.encode('gb2312')):
				continue
			else:
				os.mkdir(path.encode('gb2312'))
			py = 0
			i = 0
			while i <= 10:
				cursor = db.cursor()
				sql = 'select * from car_tab_temp where HPHM = ' + '\'' + hphm + '\''
				# print sql
				cursor.execute(sql)
				results = cursor.fetchall()
				try:
					url = results[i+py][11]
					print url
				except Exception,e:
					break
				try:
					response = urllib2.urlopen(url,timeout = 1)
					webpage = response.read()
					print imghdr.what('',webpage)
					print 'ok'
					urllib.urlretrieve(url,u'%s/%d.jpg'%(path,i))
					print "image saved"
					i = i + 1
				except Exception,e:
					print 'timeout'
					py = py + 1
	except Exception,e:
		print 'Some worry happend' , e
	finally:
		db.close()
		cp_in.close()


start()
