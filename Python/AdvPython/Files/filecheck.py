import os,sys

fname = input("Enter file name\n")

if os.path.isfile(fname):
 f = open(fname,'r')
 str = f.read()
 print(str)
else:
 print(fname +' does not exist')
 exit(1)