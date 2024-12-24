#  Write a function to flatten a list of list into a single list

def flatten_list(*args):
	list2=[]
	for i in args:
		list2+=i
	return list2
l=flatten_list([1,2,3],[4,5,6],[7,8,9])
print(l)

'''
Output:
[1,2,3,4,5,6,7,8,9]
