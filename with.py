#coding=utf-8

with open("./manifest.json") as file :
	data = file.readlines()

print data[1]