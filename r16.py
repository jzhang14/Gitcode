def sum_odd(x):
	"""Sum the odd positive integers smaller than x

	>>> sum_odd(8)
	16
	>>> sum_odd(5)
	4
	"""

	return sum([k for  k in range (1,x) if k% 2 == 1])

if __name__ == '__main__':
	import doctest
	doctest.testmod()