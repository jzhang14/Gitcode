def sum_int(x):
	"""Sum the squares of positive integers smaller than x.

	>>> sum_int(4)
	14
	"""
	sum2 = [k*k for k in range(1,x)]

	return sum(sum2)

if __name__ == '__main__':
	import doctest
	doctest.testmod()