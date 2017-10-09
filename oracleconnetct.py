#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cx_Oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8' 

db=cx_Oracle.connect('si01','jp2011','100.11.44.237:1521/SICSDB')#连接数据库
print db.version


cursor=db.cursor()#建立游标
cursor.execute('select * from mount_tab')
a=cursor.fetchone()
print a[3]
cursor.execute('select * from deviceinfo_tab')
a=cursor.fetchone()
print a[1]

cp_in = open('hphm.txt','r')
lines = cp_in.readlines()
cphm = lines[1].strip() #去掉换行符号
print cphm
sql = 'select * from car_tab_temp where HPHM = ' + '\'' + cphm + '\''
print sql
cursor.execute(sql)
a=cursor.fetchone()
print a[1]
db.close()