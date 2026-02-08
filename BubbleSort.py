arr = [1, 4, 2, 5, 3, 17, 11, 12]

n = len(arr)

for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)

arr = [1, 4, 2, 5, 3, 17, 11, 12]
p, q = 0, 1

while q <= len(arr) - 1:
    if arr[p] > arr[q]:
        arr[p], arr[q] = arr[q], arr[p]
    p += 1
    q += 1

print(arr)

arr = [1, 4, 2, 5, 3, 17, 11, 12]

n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
