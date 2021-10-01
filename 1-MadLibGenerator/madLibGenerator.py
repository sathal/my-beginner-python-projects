print('Project 1: Mad Lib Generator')

# Function to get input from the user
def getUserInput(wordType):
    return input('Give me a ' + wordType + ': ')

# method to denote main execution
def main():
				# The madlib poem
				madlib = '''
Now be {3} with this {4} poem:
How much {0} could a {1} {2}
If a {1} could {2} {0}?
As much {0} as a {1} could {2},
If a {1} could {2} {0}.
'''

				# Word type list
				wordTypeList = ['noun (plural)','noun (singular)','verb (Example: \'run\')','reaction (Example: \'surprised\')','adjective']

				# List to hold the user's inputs
				chosenWords = []


				# List index for use in the wordList
				listIndex = 0

				# Iterate through the wordList and get user input
				for wordType in wordTypeList:
				    chosenWords.append(getUserInput(wordType))
				    listIndex+=1

				print('\nYour choice of words is excellent: ')
				print(chosenWords)

				# Display the madlib to the console
				# Must "unpack" the List using '*'
				print(madlib.format(*chosenWords))


main()
