'''
Scriptname: librarysearch.py
Date:18/6/2018
Author:Sarath
Description: This is used to search and get the books in library or return the book based on the subject choosen
'''

import sys
import pathfile as p

books = {}
def search():
    subject1 = input("plese enter book name\n")
    with open(p.libfilename,'r') as fl:
        listlib = fl.readlines()
        for line in listlib:
            records = line.split(',')
            subject=records[0]
            no = int(records[1].split('\n')[0])
            books[subject]=no
        if (subject1 in books.keys()):
            if (books[subject1] > 0 ):
                option = input("please confirm(Y/N).Do you need %s book\n"%subject1)
                if (option=='Y'):
                    getbook(subject1)
                    sys.exit(1)
                else:
                    print("Thanks for inquiry of %s book"%subject1)
                    sys.exit(1)
            else:
                print(" %s books are not available.Better luck next time"%subject1)
                sys.exit(1)
        else:
            print(" %s books are not available in our library."%subject1)
            sys.exit(1)

def getbook(subject):
    #to get a book absed on the subject
    print("i am trying to get the %s book to read"%subject)
    books[subject] = books[subject] -1
    with open(p.libfilename,'w') as fs:
        for i in books:
            name=i
            no=books[i]
            rec = name+','+str(no)+'\n'
            fs.write(rec)

def returnbook():
    books1={}
    print("I am planning to return the book.Please take it")
    subject2=input("Please tell me the book name\n")
    with open(p.libfilename,'r') as fr:
        listlib = fr.readlines()
        for line in listlib:
            records = line.split(',')
            subject=records[0]
            no = int(records[1].split('\n')[0])
            books1[subject]=no

        if (subject2 in books1.keys()):
            books1[subject2]= books1[subject2] +1
        else:
            print("I think this %s book is not from our library.Please check once.")
            sys.exit(1)

    with open(p.libfilename,'w') as frn:
        for i in books1:
            name=i
            no=books1[i]
            rec = name+','+str(no)+'\n'
            frn.write(rec)


print("Library Management\n")
print("1.search and get the book from Library\n2.Return Book to Library\n".title())
user_opt = int(input("please select option from list\n"))
if user_opt==1:
    search()
elif user_opt==2:
    returnbook()
else:
    print("Choose correct option from available list\n")

