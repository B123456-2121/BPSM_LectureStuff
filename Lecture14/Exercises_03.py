#!/usr/bin/python

# programme/script to compare a small set of 9-base sequences, pairwise
# determining a distance score based on percent identity
# All sequences are of equal length (phew, that's good!)
# Written by s123456 on 31 Oct 2025
# --------------------------------------------------------------
#

# INPUT
input_seqs = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

# PROCESS BIT
for_range = list(range(0,len(input_seqs)))
for_range
[0, 1, 2, 3]

# Need loop for x and y accessions of pairwise comparisons, just do all of them!
# "X axis" loop
for Xaxis_item in for_range:
# Convert the first element of input_seqs into a list itself
    first_query = list(input_seqs[Xaxis_item])
# "Y axis" loop
    for Yaxis_item in for_range:
# Reset distance measure
          distance = 0
          other_query = list(input_seqs[Yaxis_item])
# Go along each base in each of the two sequences to
# compare if identical or not; score +1 if it is
          for base in list(range(0,len(first_query)))   :
             print("Index" + str(base) + ":" +  ## this one
             str(first_query[base]) + "," + str(other_query[base]) + "...")
             if first_query[base] == other_query[base]   :
                  distance = distance + 1

# OUTPUT pairwise comparison done, output details
# DON'T include the self-comparisons in the summary output
          if input_seqs[Xaxis_item] != input_seqs[Yaxis_item]   :
# Scores

               print(str(distance) + " identities between " + input_seqs[Xaxis_item] + 
               " and " + input_seqs[Yaxis_item])
# Percentages

               print("\t" + str(int(100*(distance/len(input_seqs[Xaxis_item])))) +
               " percent similarity between " + input_seqs[Xaxis_item] + " and " + input_seqs[Yaxis_item])


