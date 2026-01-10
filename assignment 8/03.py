#sum of all odd number between 1 to 10
def sum_of_odd(n):
    return sum(range(1,n+1,2))
n=int(input("Enter a number"))
print("sum of all odd number from 1 to 10:",n, "is:",sum_of_odd(n))