#!/usr/bin/python
# Function definition is here
def func_1( nlist ):
#This changes a passed list into this function
	nlist.append([10,20,30,40]);
	print "Values inside the function: ", nlist
	return
# Now you can call func_1 function
nlist = [100,200,300];
func_1( nlist );
print "Values outside the function: ", nlist