class Rectangle():
	def __init__(self, sideA, sideB):
		self.sideA = sideA
		self.sideB = sideB

	def area(self):
		return self.sideA*self.sideB


r1=Rectangle(5,10) #oi parametroi pane stin __init__ method
print(r1.sideA , r1.sideB)
print(r1.area())
