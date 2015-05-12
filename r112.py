import random
def mychoice(x):
	print len(x)
	return x[random.randrange(0,len(x))]

if __name__ == '__main__':
	q = 'qwertyuiopasdfjgkls'
	for i in range(15):
		print mychoice(q)

