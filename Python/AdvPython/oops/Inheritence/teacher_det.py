from Teacher import teacher

class student(teacher):
	def setmarks(self,marks):
		self.marks = marks
	def getmarks(self):
		return self.marks
s = student()
s.setid(1001)
s.setname('PAVAN')
s.setmarks(98)

print("student id is:",s.getid())
print("student name is ",s.getname())
print("studennt marks is",s.getmarks())
