def enclosingfun():
	m=10
	def local():
		# m=7
		print (m)
	local()
m=5
print (m)


enclosingfun()
