class book1:
	def __init__(self,price):
		self.price = price
	def __gt__(self,others):
		return self.price > others.price

class book2:
	def __init__(self,price):
		self.price = price

b1 = book1(190)
b2 = book2(150)
print("total price is ",b1 > b2)
