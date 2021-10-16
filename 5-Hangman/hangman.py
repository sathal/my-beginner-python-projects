secretWordString = 'POLYMORPHIC'
secretWord = list()
guessedLetters = list()
guessesRemaining = 5

CORRECT_GUESS = 1
WRONG_GUESS = 2
LETTER_ALREADY_GUESSED = 3


class WordLetterIndex:
	def __init__(self, letter, guessed):
		self.letter = letter
		self.guessed = guessed

def setup():
	global secretWordString
	global secretWord
	for l in secretWordString:
		secretWord.append(WordLetterIndex(l,False))

def checkGuess(guess):
	global guessedLetters
	global secretWord
	# If user guesses same letter again
	if guess in guessedLetters:
		return LETTER_ALREADY_GUESSED

	# If user guesses a new letter correctly
	for i in range(len(secretWord)):
		if guess == secretWord[i].letter and secretWord[i].guessed == False:
			guessedLetters.append(guess)
			return CORRECT_GUESS

	# User guessed a letter and it was wrong
	guessedLetters.append(guess)
	return WRONG_GUESS

def lettersRemainToBeGuessed():
	global secretWord
	guessesLeft = False

	for secretLetter in enumerate(secretWord):
		# Uncomment the below print statement to see that each secret letter returned from enumerate() is a TUPLE
		#     Output would look something like this:
		#        (0, <__main__.WordLetterIndex object at 0x104b2fb80>)
		#        (1, <__main__.WordLetterIndex object at 0x104b9a7c0>)
		#        (2, <__main__.WordLetterIndex object at 0x104b9a850>)
		#        (3, <__main__.WordLetterIndex object at 0x104b9a910>)
		#        .....
		#print(secretLetter)
		if secretLetter[1].guessed == False:
			guessesLeft = True
			break
	return guessesLeft

def renderPerson():
	global guessesRemaining

	if guessesRemaining == 0:
		return '(:()-|-<'
	elif guessesRemaining == 1:
		return '(:))-|-'
	elif guessesRemaining == 2:
		return '(:))-|'
	elif guessesRemaining == 3:
		return '(:))-'
	elif guessesRemaining == 4:
		return '(:))'
	else:
		return ''

def renderState():
	global secretWord
	global guessesRemaining
	display = renderPerson() + '\n'

	for i, item in enumerate(secretWord):
		if secretWord[i].guessed == True:
			display += secretWord[i].letter
		else:
			display += '_'
		display += ' '
	print(display + '\n')

def main():
	global secretWord
	global guessesRemaining

	setup()

	while guessesRemaining > 0:
		# Prompt user for guess
		guess = input('Guess a letter: ')
		guess = guess.upper()

		# Check user's guess - True/False
		# Respond to user about their guess
		result = checkGuess(guess)
		if result == CORRECT_GUESS:
			count = 0
			for i in range(len(secretWord)):
				if secretWord[i].letter == guess:
					count+=1
					secretWord[i].guessed = True
			if count == 1:
				print('There is one \'' + guess + '\'')
			else:
				print('There are ' + str(count) + ' ' + guess + '\'s')
		elif result == LETTER_ALREADY_GUESSED:
			print('You already guessed ' + guess + '\'')
		else:
			print('Sorry, there are no ' + guess + '\'s')
			guessesRemaining-=1

		# Render current state to console
		renderState()
		if lettersRemainToBeGuessed() == False:
			break
		if guessesRemaining == 0:
			break

	# We are outside of the while loop at this point
	if guessesRemaining > 0:
		# User wins
		print('You win!')
		#print('guessesRemaining = ' + str(guessesRemaining))
	else:
		# User loses
		print('You lose!')

main()
