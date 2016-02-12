def func(a, b, c=7, *args, **kwargs):
	print('a, b, c:', a, b, c)
	print('args:', args)
	print('kwargs:', kwargs)

func(1,2,3, *(5,7,9) , **{'A':10 , 'B':20})