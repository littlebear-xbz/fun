# encoding: utf-8
import struct
import binascii

value = (3,'qew',2.3)
s = struct.Struct('I3sf')
date = s.pack(*value)
unpackdate = s.unpack(date)

print s
print date
print unpackdate