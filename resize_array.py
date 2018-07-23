from ctypes import *


l = (c_int*2)()
l[0] = 11
l[1] = 22

print l[:]

print "1-------------------------1"
# method one, construct new array from existing array
l = (c_int*10)(*l)
print l
print l[:]
print "1-------------------------1"
resize( l, sizeof(c_int*12) )
n = (c_int*12).from_address(addressof(l))
print n[:]
