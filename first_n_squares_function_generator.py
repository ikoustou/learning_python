
def sqr_list(n):
	return [x**2 for x in range(n)]

print(sqr_list(10))

def sqr_generator(n):
	for x in range(n):
		yield x**2

sqr_temp = sqr_generator(4)

print(sqr_temp)
print(next(sqr_temp))
print(next(sqr_temp))
print(next(sqr_temp))
print(next(sqr_temp))
#print(next(sqr_temp))
#print(next(sqr_temp))
