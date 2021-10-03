from random import randint

secretNumber = randint(0,100)
#print(secretNumber)

correctlyGuessed = False

# While you have not guessed correctly continue to loop
while not correctlyGuessed :
	guess = int(input("Try to guess the random number\n"))
	
	if guess == secretNumber :
		correctlyGuessed = True
	elif guess < secretNumber:
		print("Too low!  \_(._.)_/")
	else:
		print("Too high!  \_(._.)_/")

print("You got it!")









