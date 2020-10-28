
# def surprise(arr, count):

	# for c in range(0,len(arr)):
		# arr[c] = arr[c] - count
	
		

# def main():
	
	# first_try = [1,2,3]
	# second_try = [20,30,40,50]
	
	# count = 10
	# surprise(first_try, count)
	# print(first_try)
	# print('The value of count after the first_try :-', count)
	
	# count += 10
	# surprise(second_try, count)
	# print(second_try)
	# print('The value of count after the second try :-', count)
	
	
# main()

# def main():

	# fun_yep = {}
	# the_key_list = [1,2,3,4,5]
	# value = 153
	
	# for i in the_key_list:
		# fun_yep[i+2] = value
		# value += 100
	
	# print(fun_yep)
	# print()
	# print(fun_yep.keys())
	# print(fun_yep.values())
	# print()
	# del fun_yep[3]
	# print(fun_yep)
	# fun_yep.clear()
	# print(fun_yep)


# main()

# def main():

	# word = 'Never odd or even'
	
	# word = word.lower()
	# word = word.replace(" ", "")
	
	
	# if word == word[::-1]:
		# print('True')
	# else: 
		# print('False')

# main()

# def createRowofTable(multiplier, row):
	# for i in range(0,7):
		# row[i] = (i+1) * multiplier
		

# def main():
	
	# multiplicationTable = [0,0,0,0,0,0,0]
	# for i in range(0,7):
		# createRowofTable(i+1, multiplicationTable)
		# for j in range(0,7):
			# print(multiplicationTable[j], end= '\t')
		# print()
		
	
# main()

def main():
	table = [[],[],[],[],[],[],[]]
	
	for i in range(0,7):
		for j in range(0,7):
			table[i][j] = (i+1)*(j+1)
			
	print(table)
main()

# def main():
	
	# multiplicationTable = createTable()
	
	# for i in range(0,7):
		# for j in range(0,7):
			# print(multiplicationTable[i][j], end='\t')

# main()