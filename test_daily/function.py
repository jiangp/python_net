#!/sur/bin/python
#Filename : function.py

def sayHello():
	print'Hello World!'

#sayHello()

def printMax(a, b):
	if a > b:
		print a, 'is maximum'
		return a
	else:
		print b ,'is maximum'
		return b
print printMax(3, 4)
def func():
	global x  
	print 'x is', x
	x= 2
	print 'Changed local x to', x
#func()
#print 'x is still', x

def say(message, times = 1):
	print message * times
#say('Hello')
#say('World', 5) # five times world

def funcnumber(a, b = 5, c = 10):
	print'a is: ', a, 'b is: ', b, 'c is: ', c
#funcnumber(3, 7)
#funcnumber(25, c = 24)
#funcnumber(c = 50, a =100)



