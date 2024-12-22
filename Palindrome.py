# write a program to chech if the given string is palindrome or not

input_string=input('Enter string :')
l=input_string[::-1]
if  input_string == l:
	print(input_string,'is Palindrome')
else:
	print(input_string,'is not a Palindrome')

'''
output:
Enter string :madam
madam is Palindrome
'''
