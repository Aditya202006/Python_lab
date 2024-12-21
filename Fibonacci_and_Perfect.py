# program to print the Fibonacci Sequence

n=int(input('Enter range :'))
a=0
b=1
for i in range(n):
	print(a)
	a,b=b,a+b

'''
OUTPUT

Enter range :5
0
1
1
2
3

'''

# program to check whether the given numberis Perfect Number or Not

n=int(input("Enter n value :"))
sum=0
for i in range(1,n):
	if(n%i==0):
		sum+=i
if(sum==n):
	print(n,"is a perfect Number")
else:
	print(n,"is not a perfect Number")

'''
OUTPUT

Enter n value :5
5 is not a perfect Number

'''
