#!/usr/bin/python

import os, sys, subprocess, shutil

# Get a list of the files we might want to process
# We need the path : directory and the file name.
# This loop would open each file
for file_name in os.listdir('dna_files/') : 
    if file_name.endswith('.dna') : 
        f'Reading sequences from {file_name}'
        dna_file = open('dna_files/' + file_name)
# This loop then looks at each line and gets the length
# Note the indentation...
        for line in dna_file : 
            dna = line.rstrip('\n') 
            length = len(dna) 
            print(f'\tFound a DNA sequence with length {str(length)}' )

# Now add some code that will try each size bin in turn to see if the sequence fits.
# We'll use a range to check the bounds on each size bin

# Go through each file in the directory
for file_name in  sorted(os.listdir('dna_files')) : 
# Check if the file name ends with .dna
  if file_name.endswith('.dna') : 
    print('Reading sequences from ' + file_name) 
# Open the file and process each line
    dna_file = open('dna_files/' + file_name) 
# Calculate the sequence length 
    for line in dna_file :
      dna = line.rstrip('\n') 
      length = len(dna) 
      print('\tsequence length is ' + str(length)) 
# Go through each size bin and check if the sequence belongs in it
      for bin_lower in list(range(100,1000,100)) : 
        bin_upper = bin_lower + 99 
        if length >= bin_lower and length <= bin_upper : 
          print('\t\tbin is ' + str(bin_lower) + ' to ' + str(bin_upper)) 

# We will need to create some new directories so that we can write
# each DNA sequence to the correct one based on the directory name
for bin_lower in list(range(100,1000,100)) : 
    bin_upper = bin_lower + 99 
    bin_directory_name = str(bin_lower) + '_' + str(bin_upper) 
    os.mkdir(bin_directory_name) 

# What directories do we have now? Don't want to use os.listdir() !
len(os.listdir())


# Could do this
for name in os.listdir(".") :
   if os.path.isdir(name) :
     print (name)

# Or use os.walk() to generate the names in a directory tree
mydirs = os.walk('.')
# Access the contents with a for loop
sorted([x[0] for x in mydirs])

# Let's run our programme now
# Re-create a new directory for each size bin, essentially deleting anything there previously
for bin_lower in list(range(100,1000,100)) : 
    bin_upper = bin_lower + 99 
    bin_directory_name = str(bin_lower) + '_' + str(bin_upper) 
    shutil.rmtree(bin_directory_name)
    os.mkdir(bin_directory_name) 

# create a variable to hold an arbitrary sequence identifier number
seq_number = 1

# Go through each file in the directory
for file_name in os.listdir('dna_files') : 
# Check if the file name ends with .dna
  if file_name.endswith('.dna') : 
    print('Reading sequences from ' + file_name) 
# Open the file and process each line
    dna_file = open('dna_files/' + file_name) 
    for line in dna_file :
# Calculate the sequence length 
      dna = line.rstrip('\n') 
      length = len(dna) 
      print('\tsequence length is ' + str(length))
# Go through each size bin and check if the sequence belongs in it
      for bin_lower in list(range(100,1000,100)) : 
        bin_upper = bin_lower + 99 
        if length >= bin_lower and length <= bin_upper : 
          print('\t\tbin is ' + str(bin_lower) + ' to ' + str(bin_upper)) 
          bin_directory_name = str(bin_lower) + '_' + str(bin_upper) 
          output_path = bin_directory_name + '/' + str(seq_number) + '.dna' 
          output = open(output_path, 'w') 
          output.write(dna) 
          output.close() 
# Increment the sequence number
          seq_number = seq_number+1


