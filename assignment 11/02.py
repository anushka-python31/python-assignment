#wap to Merge Two Lists and Sort it

a = [3, 1, 4]
b = [2, 5]
merged = a + b

# Bubble sort
for i in range(len(merged)):
    for j in range(len(merged) - i - 1):
        if merged[j] > merged[j + 1]:
            merged[j], merged[j + 1] = merged[j + 1], merged[j]
print("Sorted Merged List:", merged)