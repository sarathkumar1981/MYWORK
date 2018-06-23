class A:
	def method(self):
		print("This is A class")
		super().method()
class B:
	def method(self):
		print("This is B class")
		super().method()
class C:
	def method(self):
		print("This is C class")

class X(A,B):
	def method(self):
		print("This is X class")
		super().method()
class Y(B,C):
	def method(self):
		print("This is Y class")
		super().method()

class P(X,Y,C):
	def method(self):
		print("P class Method")
		super().method()


p = P()
p.method()
