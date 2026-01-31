# chars = ["a", "a", "b", "b", "c", "c", "c", "d"]
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
ans = ""
# for i in chars:
#     if chars.count(i) == 1:
#         p = i
#     else:
#         p = i + str(chars.count(i))

#     if p not in ans:
#         ans += p

p = 0
n = len(chars)
ans = ""
while p < n:
    q = p
    while q < n and chars[q] == chars[p]:
        q += 1
    charcount = q - p
    if charcount == 1:
        ans += chars[p]
    else:
        ans += chars[p] + str(charcount)
    p = q


print()
