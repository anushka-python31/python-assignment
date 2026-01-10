#wap to check whether a number is prime or not using recursion.

def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

num = int(input("Enter number: "))
print("Prime:", is_prime(num))