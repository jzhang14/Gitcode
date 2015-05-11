# import copy
# def all_possible_strings(l):
# 	print l
# 	if len(l)==1:
# 		return None
# 	if len(l)>1:
# 		for i in range(len(l)):			
# 			print i
# 			q = copy.deepcopy(l)
# 			l_candidate = q[i:len(l)-1]
# 			print l_candidate
# 			l_candidate.remove(l[i])
# 			all_possible_strings(l_candidate)

# if __name__ == '__main__':
# 	all_possible_strings('c a t'.split())
# 	# split would make the string list
import itertools
def all_possible_strings(l):
	i = 1
	while i<=len(l):
		print list(itertools.permutations(l,i))
		i = i+1

if __name__ == '__main__':
	all_possible_strings('c a t d o g'.split())
	# split would make the string list
