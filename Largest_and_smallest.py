# Write a function to find the largest and smallest numbers in a list

def largest_smallest(list1):
	largest = max(list1)
	smallest = min(list1)
	return largest,smallest
print("Largest and smallest values are :",largest_smallest([1,5,9,7,3]))

'''
Output:
Largest and smallest values are : (9, 1)
'''
