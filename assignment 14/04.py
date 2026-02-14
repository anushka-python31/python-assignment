lst = [1, 2, 3, 4, 5, 6]
target = 7
pairs = {(x, y) for x in lst for y in lst if x + y == target}
print(pairs)  # {(1, 6), (2, 5), (3, 4)}
