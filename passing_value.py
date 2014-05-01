#!/usr/bin/python
def fun(la):
    la[0]=-1
def fun2(la):
    la=-1

#a list can be changed
l1=[1,2,3]
fun(l1)
print l1

#error:'tuple' object does not support item assignment
#t1=(4,5,6)
#fun(t1)
#print t1

#will not change
sb=3
fun2(sb)
print sb

#change to a list then succeed
sb2=[3]
fun(sb2)
print sb2
