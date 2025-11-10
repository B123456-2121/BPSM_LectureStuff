# First import the libraries
import os, sys, re, numpy as np
import pandas as pd

# Get the file
os.mkdir("${HOME}/Exercises/Lecture17")
os.chdir("${HOME}/Exercises/Lecture17")

# If you opted for the new version, you could call it eukaryotes.tsv as its tab-separated values?
os.system("wget -qO eukaryotes.tsv 'ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt'")

# Read the file into a dataframe
df = pd.read_csv('eukaryotes.tsv', sep="\t", na_values=['-'])

# Create a new index which is made up of the species name and the accession number
df.index=df.apply(lambda x : "{} ({})".format(x['#Organism/Name'], x['BioSample Accession']), axis=1)

# What are the column headers
df.columns

# How many fungal species have genomes bigger than 100Mb?
# use two conditions joined with &
len( df[ (df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100) ] )

# or we could use apply
len(df[df.apply(lambda x : x['Group'] == 'Fungi' and x['Size (Mb)'] > 100, axis=1)])

# What are their names?
# Start with the same query as before, then get the names column
big_fungi = df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)]

# Transform the series object into a simple list of strings
list(big_fungi['#Organism/Name'])

# Nicer when it is sorted!
sorted(list(big_fungi['#Organism/Name']))



# How many genomes of each major group (plants, animals, fungi and protists) have been sequenced, and how many unique organisms?
# We can figure out the answer for a single group
len(df[df['Group'] == 'Plants'])

len(df[df['Group'] == 'plants'])

len(df[df['Group'].str.lower() == 'plants'])

len(df[df['Group'].str.lower() == 'PLANTS'])

len(df[df['Group'].str.upper() == 'PLANTS'])

# Remember that we are in Python3, so we can use a normal loop
for Group in ['Plants', 'Animals', 'Fungi', 'Protists']:
    count = len(df[df['Group'] == Group])
# To count unique ones, we could get the names and turn them into a set
    count_unique = len(set(df[df['Group'] == Group]['#Organism/Name']))
# OR we could use the drop_duplicates method which may be clearer to read
    count_unique = len(df[df['Group'] == Group].drop_duplicates('#Organism/Name'))
    print("{} genomes for {} ({} unique)".format(count, Group, count_unique))

# Which Heliconius species genomes have been sequenced, and how many scaffolds is each assembly in?
# here we HAVE to use apply
hel = df[df.apply(lambda x : x['#Organism/Name'].startswith('Heliconius'), axis=1)]
hel[ ['#Organism/Name', 'Scaffolds'] ]

# Which center has sequenced the most plant genomes?
df[df['Group'] == 'Plants']['Center'].value_counts().head()

# Which center has sequenced the most insect genomes?
(df['Group'] == 'Insects').value_counts()

# Oops!
(df['SubGroup'] == 'Insects').value_counts()


df[df['SubGroup'] == 'Insects']['Center'].value_counts().head()

# Add a column giving the number of proteins per gene
# first, we do the calculation
df['Proteins'] / df['Genes']

# We can assign this to a new column
df['Proteins per gene'] = df['Proteins'] / df['Genes']

# Show the results
df[ ['#Organism/Name', 'Group', 'Proteins per gene'] ].head()

# Which genomes have at least 10% more proteins than genes?
df[df['Proteins per gene'] >= 1.1][ ['#Organism/Name', 'Genes','Proteins','Proteins per gene'] ].head()

df[df['Proteins per gene'] >= 1.1][ ['#Organism/Name', 'Genes','Proteins','Proteins per gene'] ]

len(df[ df['Proteins per gene'] >= 1.1])

# More than 2.5 proteins per gene...
df[df['Proteins per gene'] >= 2.5][ ['#Organism/Name', 'Genes','Proteins','Proteins per gene'] ]
