nums = [1, 2, 3, 4, 5, 6]
target = 10
combos = {(a, b, c) for a in nums for b in nums for c in nums 
          if a < b < c and a + b + c == target}
print(combos)  # {(1, 3, 6), (1, 4, 5), (2, 3, 5)}
