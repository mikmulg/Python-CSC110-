import Die
import SL_Board
import Player

#Mikayla Mulgrew V00923052 Dec.1

# a function to simulate two players playing snakes and ladders
def main():
	
	print('SNAKES AND LADDERS')
	print()
	print('The board:')
	print()
	
	#call boardData function and display the board it creates
	print(boardData())
	
	#open and read boardConfig.txt
	board = open('boardConfig.txt', 'r')
	
	#first line in file is length of board
	board_size = int(board.readline())
	
	#snakes = board.readline()
	#ladders = board.readline()
	#board_data = SL_Board.SL_Board(board_size, snakes, ladders)
	
	board.close()
	
	#length of board * length of board gives the amount of total spaces
	#hence the value of the lastsquare
	last_square = board_size * board_size
	
	
	
	print()
	
	#initialize each player in the Player class
	player1 = Player.Player()
	player2 = Player.Player()
	
	#set each players name
	player1.set_name('Aaron')
	player2.set_name('Quinn')
	
	#set each players symbol
	player1.set_symbol()
	player2.set_symbol()
	
	#set each players symbol to a variable
	p1_symbol = player1.get_symbol()
	p2_symbol = player2.get_symbol()
	
	#an if statement to prevent both players symbol being the same letter
	if p1_symbol == p2_symbol:
	
		p1_symbol = player1.get_symbol()
		p2_symbol = player2.get_symbol()
	
	#printed statement for each player
	#stating name, symbol, and initial position
	print('Player 1 = ', player1.get_name(), '(' + p1_symbol + '):', player1.get_position())
	print('Player 2 = ', player2.get_name(), '(' + p2_symbol + '):', player2.get_position())
	 
	
	stop = 'no'
	
	#a while loop to go through each players turns until one lands on the last_square2
	while stop != 'yes':
		
		players_turn(player1)
	
		if player1.get_position() == last_square:
			stop = 'yes'
			print('WINNER', player1.get_name(), player1.get_symbol())
			
		else:	
			
			players_turn(player2)
		
			#get position of player one and two 
			player1.get_position()
			player2.get_position()
		
	
			if player2.get_position() == last_square:
				stop = 'yes'
				print('WINNER', player2.get_name(), player2.get_symbol())
			

def players_turn(player):
	
	die = Die.Die()
	
		#open and read boardConfig.txt
	board = open('boardConfig.txt', 'r')
	
	#first line in file is length of board
	board_size = int(board.readline())
	
	#snakes = board.readline()
	#ladders = board.readline()
	#board_data = SL_Board.SL_Board(board_size, snakes, ladders)
	
	board.close()
	
	#length of board * length of board gives the amount of total spaces
	#hence the value of the lastsquare
	last_square = board_size * board_size
	
	
	#throw dice
	die.throw()
	roll = die.get_faceUp()
		
	#players new position is last position plus value of the die
	new_position2 = player.get_position() + roll
		
	#check, if new position is a number larger than the last square
	if new_position2 > last_square:
		new_position2 = last_square
		
	#set player position as new position 
	player2.set_position(new_position2)
		
	#print player turn statistics
	return player.get_name(), '(' + player.get_symbol() + '):', player.get_position()
	
	
	
	


#This function can be called in your program. 	
def boardData():
	with open("boardConfig.txt","r") as fileHandle:
		size = int(fileHandle.readline().strip("\n"))
		snakeData = fileHandle.readline().split()
		for i in range(len(snakeData)):
			snakeData[i] = int(snakeData[i].strip("\n"))
		ladderData = fileHandle.readline().split()
		for i in range(len(ladderData)):
			ladderData[i] = int(ladderData[i].strip("\n"))
		
		# Convert snakes to a list of tuples
		snakes = []
		for i in range(0,len(snakeData)//2):
			snakes.append( (snakeData[2*i], snakeData[2*i+1]) )
		
		# Convert ladders to a list of tuples
		ladders = []
		for i in range(0,len(ladderData)//2):
			ladders.append( (ladderData[2*i], ladderData[2*i+1]) )
		newBoard = SL_Board.SL_Board(size,snakes,ladders)
		return newBoard

# Do not change anything below here. 		
if __name__ == "__main__":
	main()