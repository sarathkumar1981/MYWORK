import operator,functools

word="MARUTHI"
print('m' in word)
dict={1:"maruthi",2:"hanuman",3:"anji",4:"sarath"}
print("anji" in dict)
#list1 = [{'value': 'apple', 'blah': 2}, {'value': 'banana', 'blah': 3} , {'value': 'cars', 'blah':4}]
#map(operator.itemgetter('value'), listl)
#get_values = functools.partial(map, operator.itemgetter('value'))
#get_values(list1)
#map(lambda d: d.get('value', 'default value'), list1)
#for item in dict.keys():
 #   print(item)

if (4 in dict):
         del dict[4]
         dict.clear()
         print(dict)
         dict={1:"maruthi",2:"mars",3:"hanuman"}
print(dict)

x = int(input("please enter the value\n"))
if (x in dict):
    print(dict[x])

x=33
y=36
z=x
if (x is z):
    print(id(x))
    print(id(y))
    print(id(z))
    print("same")
else:
    print("not same")

b=0b1101
print(bin(b))
print(b)