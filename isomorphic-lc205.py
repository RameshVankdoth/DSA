# from collections import Counter


# def are_isomorphic(a, b):
#     a_counter = Counter(a)
#     b_counter = Counter(b)
#     return sorted(a_counter.values()) == sorted(b_counter.values())


# a = "paper"
# b = "title"

# if are_isomorphic(a, b):
#     print("YES")
# else:
#     print("NO")

a = "title"
b = "paper"
ans = []
p = 0
if len(a) != len(b):
    print(False)
while p < len(a) and p < len(b):
    count = 1
    while p + 1 < len(a) and p + 1 < len(b) and a[p] == a[p + 1] and b[p] == b[p + 1]:
        count += 1
    ans.append([a[p], b[p], count])
    p += 1

print(ans)

print(set(a))
print(set(b))
print(set(zip(a, b)))





