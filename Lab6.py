#-------------------------------------------------------------------------------
# Name:        Lab 6
# Purpose:     Program to match Username and Password
#
# Author:      Tailong Zhou Tai
#
# Created:     03/03/2014
#-------------------------------------------------------------------------------

def Login():                                # create function
    username = input("Enter Username: ")    # input from the user
    password = input("Enter Password: ")    # input from the user
    matchpassword(username, password)       # matchpassword parameters

def matchpassword(username, password):      # create function called matchpassword

    f= open("C:\Portable Python 3.2.5.1\password.txt","r")
    List = f.readlines()
    f.close()
    
    print(List)

    for x in range(0,len(List),2):
        print("List[x] = ", List[x])
        if((username.lower() +'\n' == List[x]) and (password +'\n' == List[x + 1])):
            print("MATCH")
            return 'True'
            """print("Username Matches")
            if(password +'\n' == List[x + 1]):
                #pwMatch = 'True'
                print("MATCH")
                return 'True'"""
        else:
            print("Username and Password DO NOT Match")
            return 'False'
        else:
            print("Username does not match")
            return 'False'
        if(unMatch == 'True' and pwMatch == 'True'):
            print("You are now Logged-In")
            unMatch = 'False'
            pwMatch = 'False'
        else:
            Login()

"""
    if( username.lower() == "bill" and password == "password"):# username bill and password
        print ("True") # print true if match
    else:# else statement
        print ("False")# print false if does not match
        print("\nPlease re-enter your username and password")# print reenter username and password
        Login()#calling login if does not match


#Login()#calling login function

matchpassword('a','a')
"""
"""

print(matchpassword('Bill','password'))
List = ['username\n','password\n','user\n','pass\n']
username = 'Bill'
"""
def main():
    Login()

if __name__ == '__main__':
    main()
