def check_frequency(l):
	word = l.split(' ')
	wordset = set(word)
	freq = {}
	# intialize the dict
	for i in wordset:
		freq[i] =0
	for i in word:
		freq[i] +=1
	print freq



if __name__ == '__main__':
	check_frequency('the day is sunny the the the sunny is is')
	
