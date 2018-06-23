class square:
	def __init__(self,side):
		self.side = side
	def area(self):
		print("area of square is :",self.side * self.side)

class rectangle(square):
	def __init__(self,l,b):
		self.l = l
		self.b = b
	def area(self):
		print("area of rectangle is:",self.l*self.b)


r=rectangle(10,12)
r.area()
