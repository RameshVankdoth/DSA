arr = [2, 2, 2, 2, 2]
arr2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]

print(list(set(arr)))
print(list(set(arr2)))


def removal(arr):
    idx = 1
    p = len(arr)
    for i in range(1, p):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1
    return arr[:idx]


print(removal(arr))
print(removal(arr2))
