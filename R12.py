def is_even(x):
	"""Check if x is even.

	>>> is_even(4)
	True
	>>> is_even(-5)
	False
	"""

	return x % 2 == 0

if __name__ == '__main__':
	import doctest
	doctest.testmod()