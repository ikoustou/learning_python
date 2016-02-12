from time import sleep, time

def sl03():
	sleep(.3)

def sl05():
	sleep(.5)

t=time()
sl03()
print('sl03 took: ', time()-t)


t=time()
sl05()
print('sl05 took: ', time()-t)
