#CSC 110 201809 Assignment 5
#Mikayla Mulgrew V00923052 Nov.17, 2018

#a function to count the number of words in a text file
#parameter passed to function is a list, len gets length of list
def wordTotal(wordlist):
	
	#get number of words in list using len
	num_words = str(len(wordlist))
	return num_words

#a function to assess the frequency of each unique word in a text file
#parameter wordlist is a list passed from function main
def wordFrequency(wordlist):
	
	#a new list to append converted strings to 
	new_wordlist = []
	
	#convert all strings to lowercase, append to new_wordlist
	for word in wordlist:
		word = word.lower()
		new_wordlist.append(word)
	
	#a new dictionary to add keys and values to 
	unique_dict = {}
	
	#for each word in new_wordlist, add all unique words once, assign to dict key
	#count the frequency of each word in new_wordlist, assign to dict value
	for word in new_wordlist:
		if word not in unique_dict:
			unique_dict[word] = new_wordlist.count(word)
	
	#return dictionary of word frequency, key = word, value = frequency\
	return unique_dict
	
	
#a function to count the number of upper and lower cases letters that appear in the text file
#parameter wordlist is a list passed from the function main
def letterCount(wordlist):
	
	#a list to append each individual character to
	new_wordlist = []
	
	#seperate each word into individual characters and append to a new list
	for word in wordlist:
		for char in word:
			if char.isalnum():
				new_wordlist.append(char)
	
	#intialize a counter for uppercase and lowercase
	count_upper = 0
	count_lower = 0
	
	for character in new_wordlist:
		if character.isalpha():
			if character.islower():
				count_lower += 1
			else:
				count_upper += 1
	
	#returns two values as a tuple
	return count_upper,count_lower

	
#a function to determine the frequency of each character that appears in the text file
#seperated into lowercase, uppercase, and numbers
#parameter is a list passed from the main function
def letterFrequency(wordlist):
	
	#a list to append each individual character to 
	new_wordlist = []
	
	#seperate each word into individual characters and append to new list
	for word in wordlist:
		for char in word:
			if char.isalnum():
				new_wordlist.append(char)
	
	#a list to append each unique character to 
	letter_dict = {}
	
	#append each unique character to empty dictionary as key 
	#value is the frequency of the word in new_wordlist
	for character in new_wordlist:
		if character not in letter_dict:
			letter_dict[character] = new_wordlist.count(character)
			
	return letter_dict

#a function to open a given file
#writes all information collected from called functions into an output file
def main():

	#open file storyIn.txt to read
	story = open('StoryIn1.txt', 'r')
	
	#create an empty list to append the words found in text file
	wordlist = []
	
	#sort through characters, rid of non alphabetical and numerical characters
	#append words to empty list
	line = story.readline()
	
	while line:
	
		word1 = line.strip()
		words = word1.split(' ')
		
		for word in words:
			for char in word:
				if char in ',.!?:;)(':
					word = word.replace(char,'')
			
			wordlist.append(word)
				
		line = story.readline()
	
	story.close()
	
	analysis_file = open('analysisOut.txt', 'w')
	
	
	#call on specified functions
	#write to an output file
	
	#print the value returned from wordTotal	
	line1 = 'Words:' + wordTotal(wordlist)
	analysis_file.write(line1 + '\n')
	
	#use returned dictionary from wordFrequency 
	unique_dict = wordFrequency(wordlist)
	
	#print values and keys in specified format
	for word in sorted(unique_dict):
		value = str(unique_dict[word])
		letter_freq = value + ': ' + word
		analysis_file.write(letter_freq + '\n')
	
	#use two values returned from letterCount
	#first is upper_count, second is lower_count
	count = letterCount(wordlist)
	uppercase = 'Upper Case Letters: ' + str(count[0])
	lowercase = 'Lower Case Letters: ' + str(count[1])
	analysis_file.write(uppercase + '\n')
	analysis_file.write(lowercase + '\n')
	
	#use returned dictionary from letterFrequency
	letter_dict = letterFrequency(wordlist)
	
	#print keys and values in specified format
	for character in sorted(letter_dict):
		value = str(letter_dict[character])
		characterlines = (character + ': ' + value)
		analysis_file.write(characterlines + '\n')
	
	analysis_file.close()
	
	
# Do not change *anything* below this line
if __name__ == "__main__":
	main()
	