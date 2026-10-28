#!/usr/bin/python3
# Program to take a DNA sequence and calculate A+T content
# Written by s123456 on 27 Oct 2026
# -------------------------------------------- #
# Input
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
# Process
at_content = (my_dna.count('A') + my_dna.count('T')) / len(my_dna)
# Output
print("A+T content is",str(int(100*at_content)),"percent")
