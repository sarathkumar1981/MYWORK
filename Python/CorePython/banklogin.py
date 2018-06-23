import sys

#bank_name = sys.argv[1]

bankdata = {"ICICI_1":"maruthi","HDFC_1":"anji","AXIS_1":"hanuman"}
print("welcome to ",bank_name)

user_name = input("Enter username\n")

#print("the user name is ",user_name)
pwd = input("Enter password\n")
#print("the pwd is \n",pwd)
#&& ( pwd in bankdata.values())
if (  (user_name in bankdata.keys())):
    if ( pwd == bankdata[user_name]):
         print("log in succesful")
    else:
        print("log in failed")
        sys.exit(1)
else:
    print("login failed")
    sys.exit(1)
            

print("Hello Mr.",user_name)
print("Thanks for visiting",bank_name)
