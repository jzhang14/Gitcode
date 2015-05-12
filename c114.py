def distinct_odd(x):
	"""Check if there only exists one distinct pair of values whose product is odd
	>>> distinct_odd([1,3,2,4,8])
	True
	>>> distinct_odd([1,3,5,2,4])
	False
	>>> distinct_odd([2,2,4,2,4])
	False
	
	"""

	pair_flag =  len([k for  k in x if k %2 == 1])
	return pair_flag ==2


if __name__ == '__main__':
	import doctest
	doctest.testmod()
