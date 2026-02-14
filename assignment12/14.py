s = "apple banana apple orange banana apple"
words = s.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)  # {'apple': 3, 'banana': 2, 'orange': 1}
