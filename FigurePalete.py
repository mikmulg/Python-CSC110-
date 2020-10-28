# Edit this file for Assignment #3
#Mikayla Mulgrew V00923052 Oct.19, 2018

#function outputs rectangle figure
#created with users specifications for height, width, and symbol
def rectangle(symbol, height, width):
	for x in range(height):
		print(symbol + '.', end='')
		for y in range(width - 1):
			print(symbol + '.', end='')
		print('')

#function outputs square figure
#created with users specifications for width and symbol
def square(symbol, width):
	for x in range(width):
		print(symbol + '.', end='')
		for y in range(width - 1):
			print(symbol + '.', end='')
		print('')

#function outputs horizontal line 
#created with users specifications for length and symbol
def horizLine(symbol, length):
	for x in range(length):
		print(symbol + '.', end='')
	print('')

#function outputs vertical line
#created with users specifications for length and symbol
def vertLine(symbol, length):
	for x in range(length):
		print(symbol + '.')

#function outputs left top triangle figure
#created with users specifications for height and symbol 
def leftTopTriangle(symbol, height):
	for x in range(height):
		print((symbol + '.') * (height - x), end='\n')

#function outputs right bottom triangle figure
#created with users specifications for height and symbol
def rightBottomTriangle(symbol, height):
	for x in range(height):
		print(((height - x - 1) * '_.') + ((x + 1) * (symbol + '.')))

#function outputs a diamond figure
#created with users specifications for width and symbol
def diamond(symbol, width):
	
	if width%2 == 0:
		for x in range(0, width//2):
			print((width//2 -x)*('_.') + (2*x + 1)*(symbol + '.'))
		for x in range(width//2):
			print((x + 1)*('_.') + (width - 2*x - 1)*(symbol + '.'))
	else:
		for x in range(0, width//2):
			print((width//2 - x)*('_.') + (2*x + 1)*(symbol + '.'))
		for x in range(1):
			print(width * (symbol + '.'))
		for x in range(width//2, 0, -1):
			print((width//2 - x + 1)*('_.') + (2*x - 1)*(symbol + '.'))

	
	
#function shows menu to user for different shapes
#gets user input for desired figures
def main(): 
	
	print('I N T E G E R   F I G U R E S')
	print()
	print()
	print('   1: Rectangle')
	print('   2: Square')
	print('   3: Diamond')
	print('   4: Horizontal Line')
	print('   5: Vertical Line')
	print('   6: Triangle (top left)')
	print('   7: Triangle (bottom right)')
	print()
	print('Input Line 1: 1-7 specifies shape (0 to end)')
	print('Input Line 2: Symbol (0-9)')
	print('Input Line 3: Shape size (integer)')
	print('Input Line 4 (for rectangle): Shape width (integer)')
	print()
	
	#get user input for shape wanted
	shape = int(input('Line 1: '))
	
	#while loop stops program when user enters 0
	while shape != 0:
	
		#if elif corresponds to menu above
		#calls on appropriate function to create shape user wants
		#gets user input for each shapes size
		if shape == 1:
			symbol1 = str(input('Line 2: '))
			height1 = int(input('Line 3: '))
			width1 = int(input('Line 4: '))
			print()
			rectangle(symbol1, height1, width1)
		elif shape == 2:
			symbol2 = str(input('Line 2: '))
			width2 = int(input('Line 3: '))
			print()
			square(symbol2, width2)
		elif shape == 3:
			symbol3 = str(input('Line 2: '))
			width3 = int(input('Line 3: '))
			print()
			diamond(symbol3, width3)
		elif shape == 4:
			symbol4 = str(input('Line 2: '))
			length4 = int(input('Line 3: '))
			print()
			horizLine(symbol4, length4)
		elif shape == 5:
			symbol5 = str(input('Line 2: '))
			length5 = int(input('Line 3: '))
			print()
			vertLine(symbol5, length5)
		elif shape == 6:
			symbol6 = str(input('Line 2: '))
			height6 = int(input('Line 3: '))
			print()
			leftTopTriangle(symbol6, height6)
		elif shape == 7:
			symbol7 = str(input('Line 2: '))
			height7 = int(input('Line 3: '))
			print()
			rightBottomTriangle(symbol7, height7)
		
		print()
		shape = int(input('Line 1: '))
		

# *** Do not edit anything below this line ***
if __name__ == "__main__":
	main()