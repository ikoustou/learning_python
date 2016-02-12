def func1(**col):
	print (col)
	for i in col:
		print (col[i])

dict1=dict(name='John' , age=40 , job ='dev')

dict2=dict(name='Stella', age=35 , job='IT', mother=True)


func1(**dict1)
print('\n next \n')
func1(**dict2)
