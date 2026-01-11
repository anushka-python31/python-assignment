#Write a program to find the sum of the following series using recursive functions:
# 1!+2!+3!+4!+...........+n! 
#Note: for fact and sum two recursive functions

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Recursive function to calculate sum of factorials
def sum_of_factorials(n):
    if n == 0:
        return 0
    return factorial(n) + sum_of_factorials(n - 1)

# Example usage
n = int(input("Enter a number: "))
result = sum_of_factorials(n)
print(f"Sum of factorials from 1 to {n} is: {result}")