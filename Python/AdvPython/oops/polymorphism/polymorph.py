class book1:
	def __init__(self,price):
		self.price = price
	def __gt__(self,b):
		return self.price > b.price


class book2:
	def __init__(self,price):
		self.price = price

b1 = book1(100)
b2 = book2(150)



if (b1>b2):
	print("b1 price is high")
else :
	print("b2 price is high")
