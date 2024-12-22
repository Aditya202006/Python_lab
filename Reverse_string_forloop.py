# Write a python program to reverse a given string without using a slicing operator 

input_string=input('Enter a String :')
reverse=""
for i in input_string:
	reverse = i + reverse
print('Reversed string is ',reverse)

'''
output:
Enter a String :java
Reversed string is avaj
'''
