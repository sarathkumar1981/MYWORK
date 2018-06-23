class Student:
    def __init__(self):
        self.name = 'Ramu'
        self.age = 25
        print("my name is QT")

    def talk(self):
        print("name is ",self.name)
        print("age is ",self.age)

s1=Student()
print(id(s1))
s1.talk()

class employee:
	name = 'phani'
	Institute = 'QT'
	def __init__(self):
		print("student name is %s and institute is %s"%(self.name,self.Institute))
	def details(s3):
		s3.name='Raji'
		s3.Institute= 'ISB'
		print("student name is %s and institute is %s"%(s3.name,s3.Institute))
s2 = employee()
s2.details()


class student3:
	name='RAVI'

s1 = student3()
s2 = student3()
s3 = student3()
s3.name = 'MARUTHI'
student3.name = 'Ramu'
s2.name = 'Lakshmi'


print(s1.name)
print(s2.name)
print(s3.name)


