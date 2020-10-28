
import SL_Board
import Die
import Player


def main():

	board = open('boardConfig.txt','r')
	
	board_length = int(board.readline())
	snakes = (board.readline())
	ladders = (board.readline())
	
	board_data = SL_Board.SL_Board(board_length, snakes, ladders)
	
	print(snakes)
	print(ladders)

	board.close()
	
	
main()

