arr = [12, 1, 134, 6, 8, 9, 90, 45, 6, 7]
total_even, total_odd = 0, 0

for i in arr:
    if i % 2 == 0:
        total_even += 1
    else:
        total_odd += 1
print(f"{total_even} Even and {total_odd} odd")
