mob= input("please enter valid mobile number\n")
if (len(str(mob)) !=10):
    print("please enter valid mobile number")
elif (mob.isdigit()):
    print("this is valid mobile number")
else:
    print("invalid mobile num")


part1="337"
part2="38"
part3="6789"

ssn= '{}-{}-{}'.format(part1,part2,part3)
print(ssn)

fruits =['pineapple','apple','banana']
fruits1=sorted(fruits)
print(fruits1)
print(fruits)
        
