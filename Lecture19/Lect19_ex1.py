# Make a chart which shows the AT content in a sliding window
# Written by s123456 on 19 Nov 2024
import os
import matplotlib.pyplot as plt
# Open the file, read it, and remove the newlines to get one long string
# then take the first 100000 characters
genome = open("/localdisk/data/BPSM/Lecture19/ecoli.txt").read().replace('\n', '').upper()
len(genome)

# Set sliding window size
window = 1000
# Regions wanted
regions=[50000,100000,len(genome)]
# Iterate over all the regions

for region in regions :
  print("Processing the region from zero to",region)
  # A list to hold the numbers
  at = []
  # Iterate over all the starting positions
  for start in range(region - window):
    win = genome[start:start+window]
    at.append(  (win.count('A')+win.count('T')) / window)
  # Plot the list with appropriate labels
  plt.figure(figsize=(20,10))
  plt.plot(at, label="AT content",linewidth=3,color="purple")
  plt.ylabel('Fraction of bases')
  plt.xlabel('Position on genome')
  plt.title("AT content, 1kb windows of the E.coli genome")
  plt.legend()
  plt.savefig("Chart_Exercise_1_"+str(region)+".png",transparent=True)
  plt.show()




