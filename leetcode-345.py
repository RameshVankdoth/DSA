letters = "leetcode"
v = "aeiou"

s = [i for i in letters]
p, q = 0, len(s) - 1
while p < q:
    if s[p].lower() in v:
        while s[q].lower() not in v:
            q -= 1
        s[p], s[q] = s[q], s[p]
    p += 1
    q -= 1

print("".join(s))
