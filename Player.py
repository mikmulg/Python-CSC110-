#Mikayla Mulgrew V00923052 Dec.1

#The Player class sets a players name and symbol, initializes there position on the board 
#and keeps track of there position on the board

import random

class Player:

	
	def __init__(self):
		
		#initializes name and symbol as empty strings, and position as 1
		self.__name = ''
		self.__symbol = ''
		self.position = 1
		
	
	def set_name(self, name):
	
		#parameter passed as name changes empty string to desired name
		self.__name = name
		
	
	def set_symbol(self):
		
		#generates a random number between 0 and 25
		number = random.randint(0,25)
		
		#a list of all the letters in the alphabet
		letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		
		#randomly generated number is inserted in the letters index to generate a random letter
		symbol = str(letters[number])
		
		#symbol is changed to the randomly generated letter
		self.__symbol = symbol
		
	def get_symbol(self):
		
		#returns the new symbol
		return self.__symbol
		
		
	def get_name(self):
		
		#returns the new name
		return self.__name
		
		
	def set_position(self, position):
		
		#takes parameter position to change self.position, gives new position
		self.position = position
		
		
	def get_position(self):
		
		#returns current position
		return self.position
		
	def __str__(self):
		
		#returns a string that states each players name, symbol, and initial position
		return 'value of' + self.__name + '(value of' + self.__symbol + '):' + str(self.position)
	
	
		
		
		