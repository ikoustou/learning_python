def func1(**col):
	print (col)
	for n in col:
		print (n, col[n])

dict1=dict(name='John' , age=40 , job ='dev')

dict2=dict(name='Stella', age=35 , job='IT', mother=True)


func1(**dict1)
print('\n next \n')
func1(**dict2)
print('\n next \n')
func1(a=1,b=2)

