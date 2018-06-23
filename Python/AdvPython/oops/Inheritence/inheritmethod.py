class square:
	def __init__(self,side):
		self.side = side
	def area(self,a):
		print("area of square is : ",self.side * self.side*a)

class rectangle(square):
	
	def __init__(self,side,l,b):
		super().__init__(side)
		self.l = l
		self.b = b
	def area(self, l=None):
		super().area(self.l)
		print("area of rectangle is: ",self.l*self.b)
	

r=rectangle(10,12,15)

r.area()
