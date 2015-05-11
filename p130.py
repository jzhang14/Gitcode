def how_many_2(n):
	"""Check how many 2 can the integer divide.
	
	>>> how_many_2(25)
	4
	>>> how_many_2(2)
	1
	"""
	p = 0
	while n>2:
		n = n/2
		p = p+1
	return p

if __name__ == '__main__':
	import doctest
	doctest.testmod()
