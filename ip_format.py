#!/usr/bin/python
import sys
f = open("ip_in.txt")
f_out = file("ip_out.txt", "w+")
lines = f.readlines()
for line in lines:
    ip_in_line = line
    ip_list = ip_in_line.split('.')
    #print lines
    for ip_i in ip_list:
        if "\n" in ip_i:
            if len(ip_i) == 3:
                ip_i = "00" + ip_i
            elif len(ip_i) == 4:
                ip_i = "0" + ip_i
            elif len(ip_i) == 5:
                ip_i = ip_i
            elif len(ip_i) == 2:
                ip_i = ""
        elif len(ip_i) == 1:
            ip_i = "00" + ip_i
        elif len(ip_i) == 2:
            ip_i = "0" + ip_i
        elif len(ip_i) == 3:
            ip_i = ip_i
        f_out.writelines(ip_i)
f.close()
f_out.close()
