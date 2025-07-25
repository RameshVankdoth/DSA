def permute(index, arr, result):
    if index == len(arr):
        result.append(arr[:])  # make a copy and store it
        return

    for i in range(index, len(arr)):
        arr[i], arr[index] = arr[index], arr[i]  # swap
        permute(index + 1, arr, result)  # recurse
        arr[i], arr[index] = arr[index], arr[i]  # backtrack


arr = [1, 2, 3]
result = []
permute(0, arr, result)
print(result)
