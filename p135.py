import random
def test_bday_paradox(n):
	p = 0.0;
	for j in range(100):
		bday  = [0]*n
		for i in range(n):
			bday[i] = int(random.uniform(1,365))
			# else it would be float
		
		bdaycheck = set(bday)
		
		if len(bday) != len(bdaycheck):
			p = p+1.0/100
	return p

if __name__ == '__main__':
	for x in range(10):

		print [5*x, test_bday_paradox(5*x)]


	
	



