# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Your Name Here
# Created: YYYY-MM-DD

# JA: You were supposed to create functions for the different parts

import math
def main():
# get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
# TODO modify this to generate a Marist-style username
    uname = first+ "." + last
# ask user to create a new password
    passwd = input("Create a new password: ")
# TODO modify this to ensure the password has at least 8 characters
    if len(passwd) <8: True
    print("Fool of a Took! That password is feeble!")
    passwd = input("Create a new password: ")
    if len(passwd) >8: False
    print("The force is strong in this one…")
    print("Account configured. Your new email address is",
    uname + "@marist.edu")
main()
