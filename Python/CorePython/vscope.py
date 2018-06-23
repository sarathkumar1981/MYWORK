class Father:
    def __init__(self):
        self.property = 500000.00
    def display_property(self):
        print("Father property =:%f"%self.property)

class son(Father):
	def __init__(self):
		self.property = 200000.00
	def display(self):
		print("son property =: %f"%self.property)

s = son()
s.display_property()
