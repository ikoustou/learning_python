from time import sleep, time

def sl03():
	sleep(.3)

def sl05():
	sleep(.5)

def measure(func):
	t=time()
	func()
	print(func.__name__, ' took: ', time() -t)

measure(sl03)
measure(sl05)