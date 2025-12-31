arr = [12, 1, 134, 6, 8, 9, 90, 45, 6, 7]

min_val = float("inf")
max_val = float("-inf")

for i in arr:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print(max_val)
print(min_val)
