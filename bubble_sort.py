arr = [1, 5, 6, 3, 4, 10, 23, 52, 1, 6, 40]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)
