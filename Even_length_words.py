# write a python program to print even length words in a string

n=input('Enter a string :').split()
for i in n:
	if len(i)%2 == 0:
		print(i)

'''
output:
Enter a string :Hi hello good morning
Hi
good
'''
