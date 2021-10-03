import inspect
import sys
from random import randint



friendX = randint(0,2)
friendY = randint(0,1)

#print('Location of the friend:')
#print(friendX,friendY)

# Move Options - changes depending on the current room one is in
moveOptionsList = []

# Move Options
UP_STAIRS = 'u'
DOWN_STAIRS = 'd'
FACE_LEFT = 'tl'
FACE_RIGHT = 'tr'
RETURN_TO_PREVIOUS_ROOM = 'r'
ENTER_DOOR = 'e'
IDENTIFY_ROOM = 'i'
GIVE_UP = 'g'
CHECK_TIME = 't'
COMPASS = 'c'
SEARCH_FOR_FRIEND = 's'
PRINT_MOVE_OPTIONS = 'p'

moveOptionsList.append(UP_STAIRS)
moveOptionsList.append(DOWN_STAIRS)
moveOptionsList.append(FACE_LEFT)
moveOptionsList.append(FACE_RIGHT)
moveOptionsList.append(RETURN_TO_PREVIOUS_ROOM)
moveOptionsList.append(ENTER_DOOR)
moveOptionsList.append(IDENTIFY_ROOM)
moveOptionsList.append(GIVE_UP)
moveOptionsList.append(CHECK_TIME)
moveOptionsList.append(PRINT_MOVE_OPTIONS)
moveOptionsList.append(COMPASS)
moveOptionsList.append(SEARCH_FOR_FRIEND)


# Room Names
roomName = [['Dinning Room','Kitchen'],['Entryway','Living Room'],['Study','Library']]

# The closer to 0 the greater the liklihood of encountering a ghost
ghostEncounterProbabilityIndex = 100

def getGhostEncounterIndex():
	global ghostEncounterProbabilityIndex
	return randint(0,ghostEncounterProbabilityIndex)

def ghostEncounterResult():
	sys.exit('You ran into a Ghost!! (x_x)')

def ghostEncounterHandler():
	index = getGhostEncounterIndex()
	if index == 0:
		ghostEncounterResult()
	elif index <= 15:
		somethingMoved()
	
def somethingMoved():
	global ghostEncounterProbabilityIndex
	#print('Index: ' + str(ghostEncounterProbabilityIndex))
	print('Something moved in the shadows...')

def printMoveOptions():
	print('Here are your available moves:')
	print(UP_STAIRS + ' - Go up the stairs in the current room if any exist')
	print(DOWN_STAIRS + ' - Go down the stairs in the current room if any exist')
	print(FACE_LEFT + ' - Turn left')
	print(FACE_RIGHT + ' - Turn right')
	print(RETURN_TO_PREVIOUS_ROOM + ' - Return to previous room')
	print(ENTER_DOOR + ' - Check for a door on the wall in front of you and enter it')
	print(IDENTIFY_ROOM + ' - identify which room you\'re in')
	print(GIVE_UP + ' - abandon your friend')
	print(CHECK_TIME + ' - Check the time')
	print(COMPASS + ' - Check your compass')
	print(SEARCH_FOR_FRIEND + ' - Search the current room for your friend')
	print(PRINT_MOVE_OPTIONS + ' - Enter \'p\' for a list of possible moves')
	

# Game State
class GameState:
	def __init__(self,currentRoomPosX,currentRoomPosY,roomJustAheadPosX,roomJustAheadPosY,orientation):
		self.currentRoomPosX = currentRoomPosX
		self.currentRoomPosY = currentRoomPosY
		self.roomJustAheadPosX = roomJustAheadPosX
		self.roomJustAheadPosY = roomJustAheadPosY
		self.orientation = orientation

def announceRoom():
	global gameState
	print('...You have entered the ' + roomName[gameState.currentRoomPosX][gameState.currentRoomPosY])

def identifyRoom():
	global gameState
	print('You are in the ' + roomName[gameState.currentRoomPosX][gameState.currentRoomPosY])

def friendFound():
	global gameState
	global friendX
	global friendY
	return ((gameState.currentRoomPosX==friendX)and(gameState.currentRoomPosY==friendY))

def processMoveChoice():
	global moveOptionsList
	global gameState
	
	action = input('\nWhat will your next move be?: ')
	
	if action not in moveOptionsList:
		print('Move not allowed')
	else:
		executeMove(action)




def executeMove(action):
	global gameState
	global ghostEncounterProbabilityIndex
	
	currentRoomPosX = gameState.currentRoomPosX
	currentRoomPosY = gameState.currentRoomPosY
	roomJustAheadPosX = gameState.roomJustAheadPosX
	roomJustAheadPosY = gameState.roomJustAheadPosY
	orientation = gameState.orientation
	
	if action == UP_STAIRS:
		print('Not yet implemented')
		return False
	elif action == DOWN_STAIRS:
		print('Not yet implemented')
		return False
	elif action == FACE_LEFT:
		if gameState.orientation == 'N':
			roomJustAheadPosX = gameState.currentRoomPosX - 1
			roomJustAheadPosY = gameState.currentRoomPosY - 1
			orientation = 'W'
		elif gameState.orientation == 'E':
			roomJustAheadPosX = gameState.currentRoomPosX - 1
			roomJustAheadPosY = gameState.currentRoomPosY + 1
			orientation = 'N'
		elif gameState.orientation == 'S':
			roomJustAheadPosX = gameState.currentRoomPosX + 1
			roomJustAheadPosY = gameState.currentRoomPosY + 1
			orientation = 'E'
		elif gameState.orientation == 'W':
			roomJustAheadPosX = gameState.currentRoomPosX + 1
			roomJustAheadPosY = gameState.currentRoomPosY - 1
			orientation = 'S'
		else:
			sys.exit('ERROR')
	elif action == FACE_RIGHT:
		if gameState.orientation == 'N':
			roomJustAheadPosX = gameState.currentRoomPosX + 1
			roomJustAheadPosY = gameState.currentRoomPosY - 1
			orientation = 'E'
		elif gameState.orientation == 'E':
			roomJustAheadPosX = gameState.currentRoomPosX - 1
			roomJustAheadPosY = gameState.currentRoomPosY - 1
			orientation = 'S'
		elif gameState.orientation == 'S':
			roomJustAheadPosX = gameState.currentRoomPosX - 1
			roomJustAheadPosY = gameState.currentRoomPosY + 1
			orientation = 'W'
		elif gameState.orientation == 'W':
			roomJustAheadPosX = gameState.currentRoomPosX + 1
			roomJustAheadPosY = gameState.currentRoomPosY + 1
			orientation = 'N'
		else:
			sys.exit('ERROR')
	elif action == ENTER_DOOR:
		if gameState.orientation == 'N':
			currentRoomPosY = gameState.roomJustAheadPosY
			roomJustAheadPosY = gameState.roomJustAheadPosY + 1
		elif gameState.orientation == 'E':
			currentRoomPosX = gameState.roomJustAheadPosX
			roomJustAheadPosX = gameState.roomJustAheadPosX + 1
		elif gameState.orientation == 'S':
			currentRoomPosY = gameState.roomJustAheadPosY
			roomJustAheadPosY = gameState.roomJustAheadPosY - 1
		elif gameState.orientation == 'W':
			currentRoomPosX = gameState.roomJustAheadPosX
			roomJustAheadPosX = gameState.roomJustAheadPosX - 1
		else:
			sys.exit('ERROR')
	elif action == RETURN_TO_PREVIOUS_ROOM:
		print('Not yet implemented')
		return False
	elif action == IDENTIFY_ROOM:
		identifyRoom()
	elif action == GIVE_UP:
		sys.exit('Sadly, you gave up on your freind and they never made it out')
	elif action == COMPASS:
		print('Your compass is pointing to \'' + gameState.orientation + '\'')
		return False
	elif action == CHECK_TIME:
		print('Hmmm... There does not look to be any clocks in this room...')
		return False
	elif action == PRINT_MOVE_OPTIONS:
		printMoveOptions()
		return False
	elif action == SEARCH_FOR_FRIEND:
		if friendFound():
			sys.exit('You found your friend! He was in the ' + roomName[gameState.currentRoomPosX][gameState.currentRoomPosY])
		else:
			print('Your friend doesn\'t look to be in the ' + roomName[gameState.currentRoomPosX][gameState.currentRoomPosY] + '...')
			return False
	
	moveIsValid = validateMove(currentRoomPosX,currentRoomPosY)
	
	if moveIsValid:
		# Update game state
		gameState.currentRoomPosX = currentRoomPosX
		gameState.currentRoomPosY = currentRoomPosY
		gameState.orientation = orientation
		gameState.roomJustAheadPosX = roomJustAheadPosX
		gameState.roomJustAheadPosY = roomJustAheadPosY
		
		if action == ENTER_DOOR:
			print('You passed through the door into a different room...')
			announceRoom()
			ghostEncounterHandler()
			ghostEncounterProbabilityIndex-=5
		elif action == FACE_LEFT:
			print('You turned to the left...')
			ghostEncounterHandler()
			ghostEncounterProbabilityIndex-=5
		elif action == FACE_RIGHT:
			print('You turned to the right...')
			ghostEncounterHandler()
			ghostEncounterProbabilityIndex-=5
		return True
	else:
		print('Hmm... There does not appear to be a door on this wall...')
		return False
		
		
def validateMove(x,y):
	# Check whether the player would end up in an inavlid location if this move were to be made
	global gameState
	if x < 0 or x >= len(roomName):
		return False
	elif y < 0 or y >= len(roomName[0]):
		return False
	else:
		return True


	

def main():
	global gameState
	friendFound = False

	gameState = GameState(1,0,1,1,'N')

	print('You\'ve entered a haunted house to find your lost friend and they need your help. (Enter \'p\' for a list of possible moves)')

	while not friendFound:
		processMoveChoice()
			
	print('Congrats! You found your friend!')

main()
