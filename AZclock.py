# Python 3 implementation for the above approach

# Function to calculate minimum time to
# print all characters in the string
def minTime(word):
	ans = 0

	# Current element where the
	# pointer is pointing
	curr = 0

	for i in range(len(word)):
		# Find index of that element
		k = ord(word[i]) - 97

		# Calculate absolute difference
		# between pointer index and character
		# index as clockwise distance
		a = abs(curr - k)

		# Subtract clockwise time from
		# 26 to get anti-clockwise time
		b = 26 - abs(curr - k)

		# Add minimum of both times to
		# the answer
		ans += min(a, b)

		# Add one unit time to print
		# the character
		ans += 1

		curr = ord(word[i]) - 97

	# Print the final answer
	print(ans)

# Driver code
if __name__ == '__main__':
	# Given string word
	str = "zjpc"

	# Function call
	minTime(str)
	
	# This code is contributed by SURENDRA_GANGWAR.
