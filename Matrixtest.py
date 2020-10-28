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
#def outputMatrix(name, matrix, outFileHandle):

# function reads data from inputted files in main and returns them as a two dimensional list
def MatrixIn():


def main():

	#function to apply matrix arithmetic 
	print('MATRIX ARITHMETIC')
	print()
	print('Inputting Matrices A, B and D and scalar c . . . . . .')
	print('. . . . Result Written to file: MatrixResult.txt')
	print()
	
	#open file with matrix data
	matrix_file = open('MatrixIn1.txt', 'r')

	#create empty list to append data to
	list = []
	
	#read lines in matrix file
	lines = matrix_file.readlines()
	
	for line in lines:
		list.append(lines.strip(' '))
		
	#get number of lines in file, set as counter for while loop
	count = len(lines)
	
	#while loop creates lists for each matrix
	
	for i in range(0, count):
		for j in range(0, count):
		
	
	#for line in lines:
		#list.append(line.split(' '))
	
		
	#assign each new list to a seperate list using index
	list1 = list[0]
	list2 = list[1]
	scalar = list[2]
	list3 = list[3]
		
	#row and column dimensions for matrix 1
	matrix1_col = list1[0]
	matrix1_row = list1[1]
	matrix1_data = [[list1[2],list1[3]],[list1[4],list1[5]]]
	
	
	print(matrix1_data)
		
	
	

	#create matrix 1 
	 
	

# Do not change *anything* below this line
if __name__ == "__main__":
	main()
	