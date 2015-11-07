#-------------------------------------------------------------------------------
# Name:        Lab 6
# Purpose:     Program to match Username and Password
#
# Author:      Tailong Zhou Tai
#
# Created:     03/03/2014
#-------------------------------------------------------------------------------

def Login():# create function
    username = input("Enter Username: ")# input from the user
    password = input("Enter Password: ")# input from the user
    matchpassword(username, password)#matchpassword parameters

def matchpassword( username, password):# create function called matchpassword

    f= open("F:\Portable Python 3.2.5.1\password.txt","r")
    List = f.readlines()
    f.close()

    for x in range(0,len(List),2):
       if(username +'\n' == List[x]):
        print("Match")

       else:
        print("no match")






    if( username.lower() == "bill" and password == "password"):# username bill and password
        print ("True") # print true if match
    else:# else statement
        print ("False")# print false if does not match
        print("\nPlease re-enter your username and password")# print reenter username and password
        Login()#calling login if does not match


Login()#calling login function

matchpassword('a','a')
"""

print(matchpassword('Bill','password'))
List = ['username\n','password\n','user\n','pass\n']
username = 'Bill'
"""