#wap to check if given number is armstrong or not using recursive function

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def armstrong_sum(n, power):
    if n == 0:
        return 0
    digit = n % 10
    return digit ** power + armstrong_sum(n // 10, power)

def is_armstrong(n):
    power = count_digits(n)
    return n == armstrong_sum(n, power)

num = int(input("Enter number: "))
print("Armstrong:", is_armstrong(num))