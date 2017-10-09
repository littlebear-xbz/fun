#!/usr/bin/python
# encoding = utf-8

import sys
import os
import time
f_in = open("hphm.txt")
lines = f_in.readlines()
print lines
if os.path.exists("images"):
	__import__('shutil').rmtree('images')
	time.sleep(1)
	print 'rmdir images'
	os.mkdir('images')
else:
	os.mkdir('images')

for hp in lines:
	path_dir = "images/%s"%hp[:-1]
	print path_dir
	if os.path.exists(path_dir):
		print "dir %s is exists"%hp[:-1]
	else:
		os.mkdir(path_dir)

print 'end'
