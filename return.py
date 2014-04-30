#!/usr/bin/python

#return a list
def ret_test(a,b):
    l=[a,b]
    return l

def ret_test2(a,b):
#    return a tuple
#    t=(a,b)
#    return t

#    return 2 value = return a tuple
    return (a,b)

#list accepted
l1=ret_test(1,2)
print l1
    
#tuple accepted
t1=ret_test2(1,2)
print t1

#2 value accepted
x,y=ret_test2(1,2)
print x
print y
