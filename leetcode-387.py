from collections import Counter

s = "leetcode"

k = Counter(s)
for i, j in k.items():
    if j == 1:
        print(s.index(i))
        break
    else:
        continue
