
#sum of multiples of 3 and 5

# def main():

	# number = int(input('Enter a number: '))
	
	# sum = 0
	
	# for x in range(number):
		# if x%3 == 0:
			# sum += x
		# if x%5 == 0:
			# sum += x
		# if x%3 == 0 and x%5 == 0:
			# sum -= x
			
	# print(sum)
	
# main()

#fibonnaci numbers

# def main():
	
	
	# maxnum = int(input('To what number would you like to evaluate? '))
	
	# f1 = 1
	# f2 = 1
	
	# x = 0
	
	# fibnums = [1,1]
	
	# while x in range(maxnum):
		# nextnum = f1 + f2
		# fibnums.append(nextnum)
		# f1 = f2
		# f2 = nextnum
		# x += 1
	
	# sum = 0
	
	# for num in fibnums in:
		# if num%2 == 0 and num < 4000000:
			# sum += num
	
	# print(sum)
	# print(fibnums)
	
# main()

#largest prime factor

def main():
	
	number = int(input('Enter a number: '))
	
	numlist = []
	
	for x in range(2,number):
		if number%x == 0:
			numlist.append(x)
	
	factors = []
	prime_factors = []
	
	for x in numlist:
		for y in range(2, x):
			if x%y == 0:
				factors.append(x)
	
	for x in numlist:
		if x not in factors:
			prime_factors.append(x)
		
	print(prime_factors)
	
	
main()