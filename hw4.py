

def main():

	with open('MatrixIn1.txt','r') as matrix_file:
		lines = [line.split() for line in matrix_file]
		
	print(lines)
	 