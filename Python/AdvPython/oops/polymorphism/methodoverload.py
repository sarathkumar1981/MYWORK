class addition:
	def sum(self,a=None,b=None,c=None):
		if (a!=None and b!=None and c!=None):
			print("sum is ",a+b+c)
		elif (a!=None and b!=None):
			print("sum is ",a+b)
		else:
			print("please enter two are three arguments")

m = addition()
m.sum(10,20,30)
m.sum(10,20)
m.sum()
