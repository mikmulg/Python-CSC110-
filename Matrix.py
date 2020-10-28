#CSC 110 201809 Assignment 4
#Mikayla Mulgrew V00923052 Nov.5/2018

# function to add to matrices together 
# input parameters are matrices represented by two-dimensional lists
# lists are created using data read from input files in the main function
def addMatrix(one, theOther):

# function to subtract two matrices
# input parameters are matrices represented by two dimensional lists
# lists are created using data read from input files in the main function
def subtractMatrix(one, theOther):

# function to multiply a matrix by a specified scalar
# input parameters are a scalar and a matrix represented by a two dimensional list
# scalar is an integer value read from input files in the main function 
# matrix is created using data read from input files in main function
def scalarMultiply(scalar, matrix):

# function to calculate the dot product of two matrices
# input parameters are two matrices represented by two dimensional lists
# lists are created using data read from input files in main function
def dot(one, theOther):

# function writes matrix (two dimensional list) to a file 
# formats matrix with its name and = sign
def outputMatrix(name, matrix, outFileHandle):

# function reads data from inputted files in main and returns them as a two dimensional list
def MatrixIn():


def main():

	#function to apply matrix arithmetic 
	print('MATRIX ARITHMETIC')
	print()
	print('Inputting Matrices A, B and D and scalar c . . . . . .')
	print('. . . . Result Written to file: MatrixResult.txt')
	print()
	
	#open Matrix Text, 
	#strip newline character and space
	with open('MatrixIn1.txt', 'r') as matrix_file:
		lines = [line.split(' ') and line.rstrip('\n') for line in matrix_file]
	
	#get the number of lines in the file
	count = len(lines)
	
	#create an empty list to append lists to
	list = []
	
	#add each line in the file to the list as a list
	for line in lines:
		element = line.split()
		list.append(element)
	
	
	
		
		print(lists)
	
	
		
	#for n in range(0, count):
		
		
		
		#if n == 3 or n%3 == 0:
			#scalar = element
		 
		
	
	
	print(list)
	
	
# Do not change *anything* below this line
if __name__ == "__main__":
	main()
	