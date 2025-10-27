#! /usr/bin/python

# Write a programme/script that, given any DNA sequence, will print all the k-mers (e.g. 4-mers) that occur more than n times.
# Written by s123456 on 31 Oct 2025
# --------------------------------------------------------------

# INPUT a made-up test sequence, assume it's good and all the same (lower) case

sequencein = "atatatatatcgcgtatatatacgactatatgcattaattatagcatatcgatatatatatcgatattatatcgcattatacgcgcgtaattatatc"

# Possible_kmer_sizes list(range(2,int(len(sequencein)-1))) = 2 to 96
# Arbitrarily choose a smaller set (2-6) for now!
possible_kmer_sizes = list(range(2,7))
# Set the minimum frequency
kmerfound_minimum = 3

# PROCESS using a for loop for the kmer sizes
for window in possible_kmer_sizes   :
    kmersfound = []
    kmerrange = list(range(0,len(sequencein)))
# Also use a for loop for getting the kmer sequences
    for startingbase in kmerrange:
        if (startingbase+window)<len(sequencein)+1   :
            seqout = (sequencein)[startingbase:startingbase+window]
            kmersfound = kmersfound + [seqout]
# OUTPUT the frequencies of the non-redundant set of kmer sequences

    nonredundantset = list(set(kmersfound))
    for kmerfrequencies in nonredundantset   :
       if kmersfound.count(kmerfrequencies) > kmerfound_minimum :
           print("Lots! " + str(kmerfrequencies)+" "+str(kmersfound.count(kmerfrequencies)))
       else   :
           print(str(kmerfrequencies) + " " + str(kmersfound.count(kmerfrequencies)))



