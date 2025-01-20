#  Python program that calculates the sum of the first n natural numbers

n = int(input("Enter a positive integer: "))
def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum
print("The sum of the first", n, "natural numbers is:", sum_of_natural_numbers(n))

'''
OUTPUT

Enter a positive integer: 7
The sum of the first 7 natural numbers is: 28
'''
