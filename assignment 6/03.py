#    1 
#  1   1 
#  1  2  1 
# 1 3  3  1 
 
n = int(input("Enter number of rows: ")) 
 
for i in range(n): 
    # Print leading spaces 
    print(" " * (n - i - 1), end="")