words = ["apple", "banana", "apple", "orange", "banana", "apple"]
unique = set(words)
freq = {w: words.count(w) for w in unique}
print(freq)  # {'apple': 3, 'banana': 2, 'orange': 1}
