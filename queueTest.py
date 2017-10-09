#!/usr/bin/python
# encoding: utf-8
#多线程实例

import Queue

q = Queue.Queue()

for i in range(5):
	q.put(str(i)+'x')

while not q.empty():
	print q.get()