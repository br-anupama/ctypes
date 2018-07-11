#!/usr/bin/python


import ctypes
import dummy
import socket




def fill_data(examp, i):
    examp.length = i
    values = ["anu", "anupa", "anupama"]
    exs = []
    ls = []
    for val in values:
        v = ctypes.create_string_buffer(10)
        v.value = val + str(i)
        ls.append(v)
    examp.names = ((ctypes.c_char*10)*3)(*ls)
    examp.sizes = (ctypes.c_int*4)(*[i, i+1, i+2, i+3])


print "1---------------1"
obj = dummy.Classes()
obj.paper_weight = 1.34

exs = []
for i in range(5):
    ex = dummy.Example()
    fill_data(ex, i)
    exs.append(ex)
obj.num = 101

obj.EX = (dummy.Example*5)(*exs)

print "paper weight ", obj.paper_weight
print "printing Example data ...."
for i in range(5):
    print "length = ", obj.EX[i].length
    print "names ::"
    for f in range(3):
        print obj.EX[i].names[f].value
    print "sizes ::"
    for g in range(4):
        print obj.EX[i].sizes[g]
print "num ", obj.num

s = socket.socket()
s.connect(('localhost', 8080))
s.send(obj)
s.close()
