#  Write a function to define a function with multiple return values

def func(a,b,c):
	if a>b and a>c :
		return a
	elif b>a and b>c:
		return b
	else:
		return c
print(func(1,2,3))

'''
output:
3
'''
