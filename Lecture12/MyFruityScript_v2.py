#!/usr/bin/python3
# Script to compare fruit
# Version 2, 24th Oct 2025
import os
import sys
# Allow for two fruit
# NOTE_incomplete: should probably include some error traps here for wrong input etc
# first_fruit  = sys.argv[1] # commented out as not using
first_fruit = input("What is the first fruit?\n\t")
# second_fruit = sys.argv[2] # commented out as not using
second_fruit = input("What is the second fruit?\n\t")
# Standard unchanging answer output
# NOTE_incomplete: a lot more could be done here...!
print(first_fruit.upper() + " are just as nice as " + second_fruit.upper())
