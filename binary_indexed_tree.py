# Binary_indexed_tree or Fenwick tree

def getsum(bit_tree, i):
	# initilized result
	s = 0 

	# index in bit_tree is 1 more than the index in bit_tree
	i = i+1

	# Travelse ancestorsof bit_tree
	while i>0:

		s += bit_tree[i]

		# Mode index to parent node
		i -= i & (-i)
	return (s)

def updatebit(bit_tree, n, i, value):
	# index in bit_tree is 1 more than the index in bit_tree
	i += 1
	#Traverse all ancestors and add 'value'
	while i <= n:
		
		# Add value to current node od bit tree
		bit_tree[i] += value

		# Update index to the next index
		i += i & (-i)

def construct(arr, n):
	# Create and initialize bit_tree as 0
	bit_tree = [0]*(n+1)

	# Update tree
	for i in range(n):
		updatebit(bit_tree, n, i, arr[i])

	return bit_tree

if __name__ == "__main__":
	freq = [2, 1, 1, 3, 2, 5]
	bit_tree = construct(freq, len(freq))
	print ("sum of element in arr[0..5] is {}".format(getsum(bit_tree, 5)))
	freq[3] += 6
	updatebit(bit_tree, len(freq), 3, 6)
	print("Sum of elements in arr[0..5] is {}".format(getsum(bit_tree, 5)))

