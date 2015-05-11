def correct_arith(l):
	"""Check if a,b,c could be in a correct formula.

	>>> correct_arith([5,5,1])
	True
	>>> correct_arith([2,5,10])
	True
	>>> correct_arith([1,3,4])
	True
	>>> correct_arith([2,9,13])
	False
	"""
	c_flag = False
	i = 0
	a = l[0]
	b = l[1]
	c = l[2]

	while (i<=1):
		if (b+c==a) or (b-c==a) or (b*c==a) or (b/c==a):
			c_flag = True
		i = i+1
		t = a
		a = c
		c = t 
	return c_flag

if __name__ == '__main__':
	import doctest
	doctest.testmod()