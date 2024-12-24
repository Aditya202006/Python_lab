#  Write a function to find  gcd of two numbers

def func(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    else:
        return func(b,a%b);
print('GCD of two numbers is :',func(60,48))

'''
Output:
GCD of two numbers is : 12
'''
