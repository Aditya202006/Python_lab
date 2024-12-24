#  Write functions for basic Arithemtoc_operation (addition,subtraction,multipliaction,division). Create a program that takes two numbers as input and returns the result.

num1=int(input("Enter num1 :"))
num2=int(input("Enter num2 :"))
def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
print(add(num1,num2))
print(sub(num1,num2))
print(mul(num1,num2))
print(div(num1,num2))

'''
output:
Enter num1 : 4
Enter num2 : 5
9
-1
20
0.8
'''
