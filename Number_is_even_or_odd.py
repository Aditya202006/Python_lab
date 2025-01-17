#  PYTHON program that prints numbers from 1 to n and checks if they are even or odd

n=int(input("Enter the number : "))
for i in range(1, n+1):  
    if i % 2 == 0:  
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

'''
OUTPUT

Enter the number : 7
1 is odd
2 is even
3 is odd
4 is even
5 is odd
6 is even
7 is odd

'''
