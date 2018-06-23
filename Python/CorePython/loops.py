s="MARUTHI"
for x in s:
    if (x in ('A','E','I','O','U')):
        #print(x,"is vowel",end ="\n")
        print("%s is vowel"%x)
    else:
        print(x," is consonent",end = "\n")

names=("maruthi","anjaneya","hanuman")

for i in names:
    print(i[0].upper() + i[1:] )
