# write a python program to count the numberof vowels in the string

n=input('Enter a String :')
count=0
for i in n:
	if i in 'aeiouAEIOU':
		count+=1
print('Number of vowels in a string is :',count)

'''
output:
Enter a String :python
Number of vowels in a string is : 1
'''
