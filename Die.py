#Mikayla Mulgrew V00923052 Dec.1

#The Die Class simulates rolling a die 

import random

class Die:
	
	def __init__(self):
		
		#initializes face up value as 0
		self.__faceUp = 0
	
	
	def throw(self):
		
		#generates a random number between 1 and 6
		num = random.randint(1,6)
		
		#reassigns the face up value based on the randomly generated number
		if num == 1:
			self.__faceUp = 1
		elif num == 2:
			self.__faceUp = 2
		elif num == 3:
			self.__faceUp = 3
		elif num == 4:
			self.__faceUp = 4
		elif num == 5:
			self.__faceUp = 5
		elif num == 6:
			self.__faceUp = 6
	
	
	def get_faceUp(self):

		#returns the new face up value
		return self.__faceUp
