#!/usr/bin/python


import ctypes
import dummy
import socket


obj = dummy.Example()
print "dir ", dir(obj), "#######", dir(obj.length)
print "len >>..",  obj.length, "dir ", dir(obj.length)
obj.length = 2
obj.sizes = (ctypes.c_int*4)(*[11, 22, 33, 44])



print "length ", obj.length

for i in range(4):
    print obj.sizes[i]


print dir(obj)
values = ["name", "qqq", "aaaaa"]
ls = []
for val in values:
   v = ctypes.create_string_buffer(10)
   v.value = val
   ls.append(v)


obj.names = ((ctypes.c_char*10)*3)(*ls)

print "1---------------1"
for i in range(3):
     print obj.names[i].value


s = socket.socket()
s.connect(('localhost', 8080))
s.send(obj)
buff = s.recv(ctypes.sizeof(dummy.Good))
gd = dummy.Good.from_buffer_copy(buff)
print "GOOD rate ", gd.rate
print "GOOD Validity ", gd.validity
s.close()

