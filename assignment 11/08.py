#wap to Print 1 to 100 in Snakes and Ladders Pattern

for i in range(1, 101, 10):
    row = []
    for j in range(10):
        row.append(i + j)
    if (i // 10) % 2 == 0:
        row.reverse()
    print(row)