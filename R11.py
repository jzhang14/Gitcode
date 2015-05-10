def is_multiple(n,m):
 	"""Check if n is a multiple of m.
	
	>>> is_multiple(3,2)
	False
	>>> is_multiple(725,5)
	True
	"""
	return n%m == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()