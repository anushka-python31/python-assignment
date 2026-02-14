words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = {}
for w in words:
    key = "".join(sorted(w))
    anagrams.setdefault(key, []).append(w)
print(list(anagrams.values()))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
