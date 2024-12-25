# Write a function to find the second largest numbers in a list

def second_largest(list1):
	largest = max(list1)
	list1.remove(largest)
	second_largest = max(list1)
	return second_largest
l=second_largest([1,3,6,7,8])
print(l)

'''
Output:
7
