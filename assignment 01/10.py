#wap to calculate area of an eqilateral triangle
import math

# Area of equilateral triangle = (√3 / 4) * side^2

side = float(input("Enter the side : "))
length = float(input("Enter the  length: "))
area = (math.sqrt(3) / 4) * (side ** 2)

print("Area of equilateral triangle =", area)
