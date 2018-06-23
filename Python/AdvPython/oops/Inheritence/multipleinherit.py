class A:
    def meth(self):
        print("This is A class")
        super().__init__()
class B:
    def __init__(self):
        print("This is B class")
        super().__init__()
class C(A,B):
    def __init__(self):
        print("This is C class")
        super().__init__()

c = C()
c.meth()
