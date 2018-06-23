'''
script name : login_file.py
Description : File based login details validation
Author : Phani
Date : 13/06/2018
Comments:
'''

import sys
import pathfile as p


def login():
	usrnm = input("Enter username\n")
	pwd = input("Enter password\n")
	aggr = {}
	with open(p.filename,'r')as f:
		lst_lines = f.readlines()
		for lst in lst_lines:
			details = lst.split(',')
			un = details[0]
			pd = details[1].split('\n')[0]
			if( aggr.get(un) == None):
				aggr[un] = pd

	if(usrnm in aggr.keys()):
		if(pwd == aggr[usrnm]):
			print("login successfully")

	else:
		print("user not found. if you are new user please register")



def register():

	username = input("Enter username\n")
	pwd = input("Enter password\n")
	rpwd = input("Reenter password\n")

	if(pwd == rpwd):
		print("Thanks for registered")
	else:
		print("password and re enter pwd should be same")
		sys.exit(1)

	str = username+','+pwd+'\n'
	with open(p.filename,'a')as f:
		f.write(str)

print("1.Login \n2.Register\n")

n = int(input("Enter your choice\n".title()))
if (n==1):
	login()
else:
	register()
