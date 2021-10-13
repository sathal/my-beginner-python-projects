from random import randint
import sys

continueRolling = 'r'

instructions = 'Enter \'r\' to roll, or anything else to quit: '

def printOne():
	print('''
_______
|     |
|  0  |
| ___ |
''')

def printTwo():
	print('''
_______
|    0|
|     |
|0___ |
''')

def printThree():
	print('''
_______
|    0|
|  0  |
|0___ |
''')

def printFour():
	print('''
_______
|0   0|
|     |
|0___0|
''')

def printFive():
	print('''
_______
|0   0|
|  0  |
|0___0|
''')

def printSix():
	print('''
_______
|0   0|
|0   0|
|0___0|
''')

def printRoll(number):
	if number == 1:
		printOne()
	elif number == 2:
		printTwo()
	elif number == 3:
		printThree()
	elif number == 4:
		printFour()
	elif number == 5:
		printFive()
	elif number == 6:
		printSix()
	else:
		sys.exit('Unforseen Error. Exiting...')

def roll():
	printRoll(randint(1,6))

def main():
	global continueRolling
	global instructions

	while continueRolling == 'r':

		continueRolling = input(instructions)

		if continueRolling == 'r':
			roll()
		else:
			sys.exit('Goodbye!')

main()
