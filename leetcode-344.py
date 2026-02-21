s = ["h", "e", "l", "l", "o"]
p, q = 0, len(s) - 1
    
while p < q:
    s[p], s[q] = s[q], s[p]
    p += 1
    q -= 1

print("".join(s))
