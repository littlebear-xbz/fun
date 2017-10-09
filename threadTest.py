#!/usr/bin/python
# encoding: utf-8
#多线程实例

import threading
from time import ctime,sleep

def music(func):
	for i in range(5):
		print "I was listen to %s. %s" %(func,ctime())
		sleep(1)

def movie(func):
	for i in range(2):
		print "I was watch movie %s. %s" %(func,ctime())
		sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'动物世界',))
threads.append(t1)
t2 = threading.Thread(target=movie,args=(u'银河',))
threads.append(t2)

if __name__ == '__main__':
	for t in threads:
		t.setDaemon(True) #设置线程守护
		t.start() #
	t.join()#防止父线程结束导致子线程一起结束
	print 'all over %s' %ctime()