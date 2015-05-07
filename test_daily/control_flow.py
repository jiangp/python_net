#!/usr/bin/python
#Filename: control_flow.py

running  = True
number = 23
while running:
	guess =int(raw_input('Enter an integer:'))
	if guess == number:
		print'Congratulation, you guessed it.'
		print"(but you donot win any prizes!)"
	elif guess == -1:
		break
	elif guess < number:
		print'No, it is a little higher than that'
	else:
		print'No, itis a litte lower than that'

print'Done'

