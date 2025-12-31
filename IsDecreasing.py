arr = [12, 1, 134, 6, 8, 9, 90, 45, 6, 7]
# arr = [5, 4, 3, 2, 1]

is_decreasing = True

for i in range(len(arr) - 1):
    if arr[i] <= arr[i + 1]:
        is_decreasing = False
        break

print(is_decreasing)
