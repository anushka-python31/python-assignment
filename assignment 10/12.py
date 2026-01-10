#wap to create three list of number,their squares and cubes
numbers = [1, 2, 3, 4, 5]
squares = []
cubes = []
for num in numbers:
    squares.append(num * num)
    cubes.append(num * num * num)
print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:", cubes)