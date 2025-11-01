#!/usr/bin/python3
## Script to ask the user a few questions, with some
## error trapping for inappropriate answers
## v1, 7 Nov 2025, written by s1234546

## INPUTS
import os

# Clear the screen
os.system('clear')

# Comments to the screen
print ("\n\nImported os\n\n")

# Function to process and check the details that the user provides
# Arguments will come in as list from the dictionary of details provided
def personal(name,age,col,py,world) :
   import string
   print("\nYou have provided the following details:\n\tName: ",name,"\n\tAge: ",age,"\n\tFave colour: ",col,"\n\tPython preference: ",py,"\n\tFlat world: ",world)
   for character in name:
     if character not in string.ascii_letters :
       return print("\nYou are more than just a number, honestly, please start again!")
   if age > 99 or age < 3 :
      print("\n"+ name + ", I really dont think your age is credible, do you?!")
   if col.upper() != "BLACK" :
      print("\nI really like black, but",col,"is OK too!")
   else:
      print("\nI really like black too, excellent choice!")
   if py.upper()[0] != "Y" :
      print("\nI am sorry that you dont like Python")
   else :
      print("\nGlad you agree that Python is cool...")
   if world != "False" :
      return print("\nEither you really DO think the world is flat (it isnt),\nor you havent typed False in the correct Python format...\n\n")
   return "OK",print("\nAll OK, thanks a lot.")


# Process: interact with the user, storing the output in an ordered dictionary
# Check the questions are in the right order for the function (or modify function)!!
details={}
details["Name"]   = input("Hi, what is your name? ")
details["Age"]    = int(input("How old are you? "))
details["Colour"] = input("What's your favourite colour? ")
details["Python"] = input("Do you like Python? ")
details["World"]  = input("The world is flat: True or False? ")

# OUTPUTS

# This is the line we can use when the dictionary is ordered, as it is in
# our server version: Python 3.12.3
# ... passing multiple arguments
# This does still require the variables to be in the correct order for our function...
personal(*list(details.values()))

print("\n\nThis was the dictionary you set up...\n\n",details,"\n\nBye!\n\n")


