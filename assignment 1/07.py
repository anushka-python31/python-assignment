#wap to find the roots of quadratic equation
import cmath
a = float(input("a: ")) 
b = float(input("b: ")) 
c = float(input("c: "))
d = b**2 - 4*a*c
root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

print("Root1 =", root1)
print("Root2 =", root2)
