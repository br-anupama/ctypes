#!/usr/bin/python


import ctypes
import dummy



obj = dummy.Example()
obj.length = 2
obj.sizes = (ctypes.c_int*4)(*[11, 22, 33, 44])



print "length ", obj.length

for i in range(4):
    print obj.sizes[i]
