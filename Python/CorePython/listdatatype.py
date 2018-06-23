a=[100,"MARUTHI","HYD"]
a[0]=333
print(a[0] * a[0])
print (type(a))

b=("100","MARUTHI","HYD")
print(b[1] * 6)
#b[0]="103"
print (type(b))

a=range(10)
for i in range(0,33,3):
    print(i)

list1=[1,2,3,4,5]
list2=[3,7,8,9]
for item in list1:
    if item in list2:
        print("overlapping")      
else:
    print("not overlapping")
