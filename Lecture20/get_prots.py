# Programme to retrieve proteins from NCBI
# Written by s123456
# Version 1, 22 Nov 2024
# Import the required modules
from Bio import Entrez, SeqIO
import os, subprocess
Entrez.email = "s123456@ed.ac.uk"
Entrez.api_key=subprocess.check_output("echo ${NCBI_API_KEY}", shell=True).rstrip().decode()
# Define and do the search
result = Entrez.read(Entrez.esearch(db="protein", term="Mammalia COX1 complete", retmax="20"))
result

# Extract info from the results of the search
count=1
for accession in result['IdList']:
    gb_file = Entrez.efetch(db="protein",id=accession,rettype="gb")
    record = SeqIO.read(gb_file, "genbank")
    print(count,record.id+"\t"+record.description+"\t"+record.seq)
    count += 1
    if count == 6 :
      break


# What were the dictionary keys again?!
result.keys()

print("There were "+str(result['Count'])+" records found.")


# Next, we want to get the length for each of the first five. 
# The easiest way to do this is to get the sequence, then use len(sequence) to get the length, 
# keeping a tally as we go so that we can work out the mean length.

# Programme to retrieve proteins from NCBI
# Written by s123456
# Version 2, 22 Nov 2024

# Import the required modules
from Bio import Entrez, SeqIO
import os, subprocess
Entrez.email = "s123456@ed.ac.uk"
Entrez.api_key=subprocess.check_output("echo ${NCBI_API_KEY}", shell=True).rstrip().decode()

# Define and do the search
result = Entrez.read(Entrez.esearch(db="protein", term="Mammalia COX1 complete", retmax="20"))

# Include a counter and a variable to hold the total length
loopcounter = total_length = 0

# Extract info from the results of the search,
# recalculating the mean length as we go
for accession in result['IdList']:
    loopcounter += 1
    gb_file = Entrez.efetch(db="protein",id=accession,rettype="gb")
    record = SeqIO.read(gb_file, "genbank")
    total_length =  total_length + len(record.seq)
    mean_length = int(total_length/loopcounter)
    print(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+record.seq[0:10]+"...")

# Output some useful info
print("There were "+str(result['Count'])+" records found.")
print("The mean length was "+str(mean_length)+" amino acids.")


# We can now turn this code into a function that takes a taxonomic name and 
# a gene name and returns the average length of the first x number (user-defined) 
# results; we'll also keep the outputs and write the info out to a file too.

# Programme to retrieve proteins from NCBI
# Written by s123456
# Version 3, 22 Nov 2024
#

# Set up a list object to hold the outputs all the session's searches
search_results = []

# Function with three arguments: taxonomic group (text, not taxid), gene name, number to return)
# NOTE_incomplete: could add another argument to cater for DNA or protein database search?
# NOTE_incomplete: could add another argument to cater for user email address?
def get_average_length(taxonomy, gene, howmany=10):
    from Bio import Entrez, SeqIO
    import os, subprocess
    Entrez.email = "s123456@ed.ac.uk"
    Entrez.api_key=subprocess.check_output("echo ${NCBI_API_KEY}", shell=True).rstrip().decode()
    search_term = taxonomy + " " + gene + " complete"
# Set up output file, named after search used (spaces removed!)
    search_output = open(search_term.replace(" ","_")+"_outputs.txt","w")
    mysearch = Entrez.esearch(db="protein", term=search_term, retmax=howmany)
    result = Entrez.read(mysearch)
    loopcounter = total_length = 0
# Extract info from the results of the search
    for accession in result['IdList']:
      loopcounter += 1
      gb_file = Entrez.efetch(db="protein",id=accession,rettype="gb")
      record = SeqIO.read(gb_file, "genbank")
      total_length =  total_length + len(record.seq)
# Add the results of the search to search_results
      search_results.append([search_term,record.id,record.description,len(record.seq),record.seq])
# Show the results (trimmed sequence) of the search to screen as we go
      print(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+record.seq[0:50]+"...")
# Write results to search output file
      search_output.write(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+str(record.seq)+"\n")
# Interim print statment for mean length
    mean_length = int(total_length/loopcounter)
    return print(("\nThe mean length was "+str(mean_length)+" amino acids.\n"))
    close(search_output)




# Programme to retrieve proteins from NCBI
# Written by s123456
# Version 4, 22 Nov 2024
#
# Dealing with X amino acids
search_results = []

# Improved function?
def get_average_length2(taxonomy, gene, startat=0,howmany=100):
    from Bio import Entrez, SeqIO
    Entrez.email = "s123456@ed.ac.uk"
    Entrez.api_key=subprocess.check_output("echo ${NCBI_API_KEY}", shell=True).rstrip().decode()
    search_term = taxonomy + " " + gene + " complete"
    search_output = open(search_term.replace(" ","_")+"_outputs.txt","w")
    mysearch = Entrez.esearch(db="protein", term=search_term, retstart = startat, retmax=howmany)
    result = Entrez.read(mysearch)
    print("Search done,", result['Count'],"found, starting retrieval of",howmany,"starting at",startat)
    loopcounter = poorseqs = total_length = 0
    for accession in result['IdList']:
      loopcounter += 1
      genbank = Entrez.efetch(db="protein",id=accession,rettype="gb")
      print('\r' + 'Retrieving sequence ' + str(loopcounter+startat), end="")
      record = SeqIO.read(genbank, "genbank")
      Xaa = str(record.seq).count("X")
      if Xaa > 5 :
         print(" Seq",loopcounter+startat,"contains",Xaa,"unknown amino acids:",int(100*Xaa/len(record.seq)), "percent of total!")
         poorseqs += 1
      else :
         total_length =  total_length + len(record.seq)
         search_results.append([search_term,record.id,record.description,len(record.seq),record.seq])
         # print(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+record.seq[0:50]+"...")
         search_output.write(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+str(record.seq)+"\n")
    goodseqs=loopcounter-poorseqs
    mean_length = int(total_length/goodseqs)
    return print(("\nThe mean length of the "+str(goodseqs)+" high quality seqs was "+str(mean_length)+" amino acids.\n"))
    close(search_output)


