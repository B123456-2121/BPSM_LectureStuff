#!/usr/bin/awk -f


# Initial values are specified in the BEGIN block
# between the BEGIN{} brackets, for example:
BEGIN {
FS="\t";OFS="_";
}

# Actions for each line of input specified
# between the {} brackets
{
count++;

# We wanted to check if the first field from the file isn't a hash symbol
if($1 != "#")
  {
print "Currently doing "count ;

# getting the third and twelth field from the file
# and doing a (somewhat meaningless) calculation
total=total + ($12 * $3)
  }
}


# Commands only done at the END of ALL inputs
# get put between END{} brackets
END{
print "The total for "count" lines was " int(total) > "awkoutputfile.txt";
print "Script run complete." >> "awkoutputfile.txt" ;
print "Script run complete."
system("ls -alrt *awk*")
}

