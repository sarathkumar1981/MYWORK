class Father:
	def __init__(self,property=0):
		self.property = property
	def display_property(self):
		print("father property is=",self.property)

class son(Father):
	def __init__(self,property1=0,property=0):
		super().__init__(property)
		self.property1 = property1

	def display_property(self):
		print("property1 =%d,property = %d"%(self.property1,self.property))
		print("the total property of child = ",self.property1 + self.property)

s = son(20000.00,80000.00)
s.display_property()
