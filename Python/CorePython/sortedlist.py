str1 = "   How many strings? \n "
print(str1.title().strip())
n = int(input())
cities = []

for i in range(n):
 str2="Enter the string"
 print(str2,end = ":")
 str3=input()
 cities.append(str3)

sorted_lst = sorted(cities)

print("sorted list is")

for i in range(n):
 print(sorted_lst[i])
 
