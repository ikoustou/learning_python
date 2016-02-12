class point():
	x=10
	y=20

p=point()

sum1=p.x+p.y
print(sum1)

p.x=30
sum1=p.x+p.y
print(sum1)

del p.x
sum1=p.x+p.y
print(sum1)