
class Student:
	marks = 10
	name = 'krishna'

	@classmethod
	def modify(k):
		k.marks += 10
		k.name = 'ravi'


s1 = Student()
s2 = Student()
print("marks in s1",s1.marks)
print("marks in s2",s2.marks)
s1.modify()
print("marks in s1",s1.marks)
print("marks in s2",s2.marks)


print(s1.name)
print(s2.name)


class Myclass:
	#this is class var or static var
	n = 0

	#constructor that increments n when an instance is  created.

	def __init__(self):
		Myclass.n = Myclass.n + 1

	@staticmethod
	def noObjects():
		print(' No.of instances created:',Myclass.n)

#create 3 instances
obj1 = Myclass()
obj2 = Myclass()
obj3 = Myclass()
Myclass.noObjects()

