from ctypes import *
import dummy

num = c_int(2)

add_num = addressof(num)

ptr = cast(add_num, POINTER(c_int))

print 
print ptr, type(ptr)
print add_num

print "==========================="

myStudent = dummy.student()
setattr(myStudent, 'name', "anupama")
setattr(myStudent, 'marks', 88)

eobj = dummy.example()

nullptr = POINTER(dummy.student)()

eobj.ptr = c_void_p(myStudent)
eobj.ptr = cast(addressof(myStudent), POINTER(dummy.student))


