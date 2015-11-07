#-------------------------------------------------------------------------------
# Name:        Lab 6
# Purpose:     Program to match Username and Password
#
# Author:      Tailong Zhou Tai
#
# Created:     03/03/2014
#-------------------------------------------------------------------------------
import sys

def Login():                                # create function
    """Function that reads a username and password and calls the
    matchpassword function to determine if the username/password
    combo match. It they do, program prints 'Match', if they do not
    match, prints 'Username and Password Do Not Match'"""
    
    username = input("Enter Username: ")    # input from the user
    password = input("Enter Password: ")    # input from the user
    if (matchpassword(username, password) == 'True'):   # matchpassword parameters
        print("Match")
        print('\n')
    else:
        print("Username and Password Do Not Match")
        print('\n')

def matchpassword(username, password):      # create function called matchpassword
    """Function that opens password.txt and reads that file into
    a list. Returns 'True' if username/password match, returns
    'False' if username/password do not match."""
        
    List = []       # Initialize list

    try:
        f = open("C:\Portable Python 3.2.5.1\password.txt","r") # opens password.txt
        List = f.readlines()    # Reads password.txt into a list
        f.close()               # Closes password.txt file
    except IOError:
        print("I/O error: Unable to read in File f") # Exception if I/O Error

    for x in range(0,len(List),2):  # Loop thru list to determine if match
        Listlower = List[x].lower()
        if((username.lower() + '\n' == Listlower) and (password + '\n' == List[x + 1])):
            return 'True'
        else:
            continue
    return 'False'

def main():
    """Main Function - calls the Login function."""
    
    Login() # Calls login functin
    switch = 1  # a switch for the while loop
    while switch == 1:
        another = input("Do you wish to enter another Username/Password y/n? ")
        if another == 'y':
            Login()
            switch == 1
        else:
            switch = 0

if __name__ == '__main__':
    main()

