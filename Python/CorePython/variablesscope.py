x = 6

def example2():
    # works
    global x
    print(x)
    print(x+5)
    z=3
    print(z)
    # but then what happens when we go to modify:
    x+=10

def example4():
    globx = x
    # now we can:
    print(globx)
    globx+=5
    print(globx)

example4()
print(x)
#print(z)
