from itertools import count
for n in count(5,10):
	if n>100 :
		break
	print (n, end=', ')
