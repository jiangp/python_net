#!/usr/bin/python
#Filename: 01.py
# open file
#f = open(r'./test.txt', 'r')
#lines = f.readlines()
#f.close()
#print lines
#if line
#a = 10

#if a is 1:
#	print "a is 1"
#elif a is 2:
#	print "a is 2"
#else:
#	print "a is other"

######while
#reply = 'repeat'
#while reply == 'repeat':
#	print 'Hello'
#	reply = raw_input('Enter "repeat" to do it again: ')

##class
#class MyClass:
#	def __init__(self,name):
#		self.name = name
#	def show(self):
#		print 'Name is ',self.name
#MyClass('Jack').show()
#class ChildClass(MyClass):
#	def show(self):
#		print "I'm child ", self.name
#ChildClass("Tom").show()
###class 
#class C:
#	count = 0;
#	def __init__(self):
#		C.count += 1
#		self.instanceCount = C.count
#def 

inputfile = open('./test.txt', 'r')
for line in inputfile:
    print line

