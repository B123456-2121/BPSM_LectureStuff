# Import the module
import re

# INPUT list of accessions
accessions = [
  'xkn59438', 
  'yhdck2', 
  'eihd39d9', 
  'chdsye847', 
  'hedle3455', 
  'xjhd53e', 
  '45da', 
  'de37dp']

# PROCESS list of accessions
# OUTPUT the ones we want
for acc in accessions:
    print(acc)

# INPUT list of accessions
accessions = [
  'xkn59438', 
  'yhdck2', 
  'eihd39d9', 
  'chdsye847', 
  'hedle3455', 
  'xjhd53e', 
  '45da', 
  'de37dp']

outputs = []

# PROCESS list of accessions
for acc in accessions: 
# contain the number 5 (could also do if '5' in acc :)
    if re.search(r'5', acc) : 
        outputs.append('contain the number 5: ' + acc)
# contain the letter d or e
    if re.search(r'[de]', acc) : 
        outputs.append('contain the letter d or e: ' + acc)
# contain the letters d and e (adjacent)
    if re.search(r'de', acc) : 
        outputs.append('contain the letter d and e (have to be adjacent): ' + acc)
# contain the letters d and e in that order (dont have to be adjacent, but can be)
    if re.search(r'd.*e', acc) : 
        outputs.append('contain the letter d and e in that order (dont have to be adjacent): ' + acc)
# contain the letters d and e in that order with a single letter between them
    if re.search(r'd.e', acc) : 
        outputs.append('contain the letter d and e in that order with a single letter between them: ' + acc)
# contain both the letters d and e in any order
    if re.search(r'd', acc) and re.search(r'e', acc) : 
        outputs.append('contain both the letters d and e in any order: ' + acc)
# start with x or y
# could have used if acc.startswith('x') or acc.startswith('y') :
# could have used if re.search(r'^[xy]', acc) :
    if re.search(r'(^x|^y)', acc) : 
        outputs.append('start with x or y: ' + acc)
# start with x or y and end with e
# could have used if (acc.startswith('x') or acc.startswith('y')) and acc.endswith('e') :
# could have used if re.search('(^x|^y).+e$',acc) :
# could have used if re.search('"[xy].+e$',acc) :
    if re.search(r'(^x|^y)', acc) and re.search(r'(e$)', acc) : 
        outputs.append('start with x or y and end with e: ' + acc)
# contains any 3 numbers in any order
    if len(re.findall(r'\d',acc)) == 3 :
        outputs.append('contains any 3 numbers in any order: ' + acc)
# contains 3 different numbers
    if len(set(re.findall(r'\d',acc))) == 3 :
        outputs.append('contains 3 different numbers: ' + acc)
# contain three or more numbers in a row
# could have used if re.search(r'[0123456789]{3,}', acc) :
    if re.search(r'\d{3,}', acc): 
        outputs.append('contain three or more numbers in a row: ' + acc)
# end with d then either a, r or p
    if re.search(r'd[arp]$', acc): 
        outputs.append('end with d followed by either a, r or p: ' + acc)

outputs.sort()
print(('\n').join(outputs))

# Could have used a dictionary approach to store all the different
# accessions etc in Key/value pairs
dict_approach = {}
dict_approach['contain the letter d or e'] = '45da'
# Adding another string, so we can just use +
# (and a comma to make it look nicer)
dict_approach['contain the letter d or e']=dict_approach['contain the letter d or e'] + ', chdsye847'

# What's there now?
dict_approach
list(dict_approach.values())
list(dict_approach.values())[0].split(',')
list(dict_approach.items())


##  DNA sequence: a double digest

# What fragment lengths will we get if we digest the sequence with a novel restriction enzyme BpsmI, whose recognition site is ANT*AAT, where * indicates the position of the cut site.
# What will the fragment lengths be if we do a double digest with both BpsmI and BpsmII (whose recognition site is GCRW*TG)?
# What are the sequences of the fragments themselves?
# What fragment lengths will we get if we digest the sequence with a novel restriction enzyme BpsmI, whose recognition site is ANT*AAT, where * indicates the position of the cut site.

# Let's write a pattern for our novel enyme BpsmI. N means any base, so the pattern is A[GATC]TAAT

# We can use re.finditer() to find the start of all the cut sites.

# Open and read the remote file (or did you copy it to a new local directory?!)
dna = open('/localdisk/data/BPSM/Lecture18/long_dna.txt').read().rstrip('\n')
len(dna)

# This goes WAY off the screen...!
dna

# Cool way to make the long string look nicer printed on the screen...
print("\n".join(re.findall('.{1,60}', dna)))
BpsmI='A[GATC]TAAT'
print('BpsmI cuts at:',BpsmI) 
# Find the sites, incrementing by three to account for where the enzyme cuts in the recognition sequence
for matching in re.finditer(BpsmI, dna): 
    print(matching.start()+3) 

# Once we've got the cut positions, we calculate the distance from the current cut site to the previous one (or to the start of the sequence).

# Start: open and read the file
dna = open('/localdisk/data/BPSM/Lecture18/long_dna.txt').read().rstrip('\n') 
last_cut = 0
findnum=0
for matching in re.finditer(BpsmI, dna):
    findnum += 1
    cut_position = matching.start() + 3
# Distance from the current cut site to the previous one
    fragment_size = cut_position - last_cut
    print('Fragment size is ' + str(fragment_size))
    last_cut = cut_position
# We also have to remember the last fragment, from the last cut to the end:
    if findnum == len(list(re.finditer(BpsmI, dna))) :
       fragment_size = len(dna) - last_cut
       print('Fragment size is ' + str(fragment_size))

# What will the fragment lengths be if we do a double digest with both BpsmI and BpsmII (whose recognition site is GCRW*TG)?
# Doing the same for two enzymes is trickier. Ambiguity code 'R' corresponds to the purines A or G, while 'W' corresponds to A or T, so we will need to 'convert' it too...

# First, define both enzymes sites
BpsmI='A[GATC]TAAT'
BpsmII='GC[AG][AT]TG'

# Make a list to store the cut positions for both enzymes
all_cuts = []
# Add cut positions for BpsmI
for match in re.finditer(BpsmI, dna): 
    all_cuts.append(match.start() + 3) 

# Add cut positions for BpsmII
for match in re.finditer(BpsmII, dna): 
    all_cuts.append(match.start() + 4)

print(all_cuts)

# These aren't in sequential order, so just sort them
all_cuts.sort()
all_cuts

# Now we can go through the list of all cuts with the same logic as before.

# Double digest run
last_cut = 0
counter = 0
for cut_position in all_cuts:
    counter +=1
    fragment_size = cut_position - last_cut
    print('Fragment '+str(counter)+' size is ' + \
       str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )
    last_cut = cut_position
# Now the last fragment
fragment_size = len(dna) - last_cut
counter +=1
print('Fragment '+str(counter)+' size is ' + \
  str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(len(dna)) )

# What are the sequences of the fragments themselves?

# We have just worked out where the enzymes cut the DNA sequence,
# so all we need to do is to use the cut positions as index positions to
# substring the dna sequence string!

# Let's use a dictionary to store the fragment sequences
fragment_sequences = {}


# Double digest run
last_cut = 0
counter = 0
for cut_position in all_cuts:
    counter +=1
    fragment_size = cut_position - last_cut
    print('Fragment '+str(counter)+' size is ' + \
       str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )
# Get the sequence substring
    fragment_sequences['Fragment'+str(counter)] = dna[last_cut:cut_position]
    print(fragment_sequences['Fragment'+str(counter)])
# Get the fragment start and end
    fragends = dna[last_cut:cut_position][0:6] + '...' + dna[last_cut:cut_position][-6:]
    print('Fragment '+str(counter)+ ' has ends: '+fragends+'\n')
    last_cut = cut_position
# Now the last fragment
fragment_size = len(dna) - last_cut
counter +=1
print('Fragment '+str(counter)+' size is ' + \
  str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(len(dna)) )
fragment_sequences['Fragment'+str(counter)] = dna[last_cut:]
print(fragment_sequences['Fragment'+str(counter)])
fragends = dna[last_cut:][0:6] + '...' + dna[last_cut:][-6:]
print('Fragment has ends: '+fragends)


# Show all the sequences
print(('\n########\n').join(list(fragment_sequences.values())))

# Are the fragments actually adjacent? Quick check!
# End of Fragment 1 ACGCGT should be next to
# beginning of Fragment 2 TGAACA
# so lets use ACGCGTTGAACA as a query against our sequence
re.search(r'ACGCGTTGAACA',dna)


