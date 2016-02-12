class Price():
	#net_price
	def final_price(self, vat, discount=0):
		return (self.net_price * (100+vat)/100)-discount

p1=Price()
p1.net_price=200
print(p1.final_price(23,10))
