s3 = ''' welcome to python
python is portable '''
print(s3)

s1="    MARUTHI    HANUMAN"
#print(s1[::-1])
#print(s1[::1])
for i in s1.strip():
   # print(i)
    print(i,end='')
print("\n")
print(s1.strip().count('U',0,6))

for i in range(len(s1)-1,-1,-1):
    print(s1[i],end ='')
print("\n")

str1 = "Welcome To Python"
print(str1)
str3 =str1.replace("python","Adv Paython")
print(str3)
str4=str3.split()
print(str4)
print(str1.upper())
print(str1.lower())
print(str1.swapcase())
print(str3.title())
print(str1.istitle())