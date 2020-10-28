
#def wordTotal(wordlist):

#def wordFrequency(wordlist):

#def letterCount(wordlist):

#def letterFrequency(wordlist):


def main():
	
	#open file storyIn.txt
	story = open('storyIn.txt', 'r')
	
	#create an empty list to append the words found in text file
	words = []
	
	#read file
	line = story.readline()
	
	while line:
		print(line)
		
		line = story.readline()
	
	#sort through characters
	#append words to empty list

main()
	
		
