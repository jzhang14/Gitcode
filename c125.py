import string
def delete_punc(l):
	"""Delete punctuations in a string.

	>>> delete_punc("Let's try, Mike.")
	'Lets try Mike'
	"""
	exclude = set(string.punctuation)
	l = ''.join(ch for ch in l if ch not in exclude)
	return str(l)

if __name__ == '__main__':
	import doctest
	doctest.testmod()