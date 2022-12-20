# Python3 implementation to
# find the character in first
# string that is present at
# minimum index in second string
import sys

# Function to find the
# minimum index character
def printMinIndexChar(st, patt):

	# unordered_map 'um'
	# implemented as hash table
	um = {}

	# to store the index of
	# character having minimum index
	minIndex = sys.maxsize

	# Lengths of the two strings
	m = len(st)
	n = len(patt)

	# Store the first index of
	# each character of 'str'
	for i in range (m):
		if (st[i] not in um):
			um[st[i]] = i

	# traverse the string 'patt'
	for i in range(n):

		# If patt[i] is found in 'um',
		# check if it has the minimum
		# index or not accordingly
		# update 'minIndex'
		if (patt[i] in um and
			um[patt[i]] < minIndex):
			minIndex = um[patt[i]]

	# Print the minimum index character
	if (minIndex != sys.maxsize):
		print ("Minimum Index Character = ",
				st[minIndex])

	# If no character of 'patt'
	# is present in 'str'
	else:
		print ("No character present")

# Driver program to test above
if __name__ == "__main__":
    st = "geeksforgeeks"
    patt = "set"
printMinIndexChar(st, patt)

# This code is contributed by Chitranayal
