arr = [4, 20, 1, 6, 30, 15, 20, 444, 85]


def sort(arr):
    for i in range(len(arr)):
        min_id = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_id]:
                min_id = j
        arr[min_id], arr[i] = arr[i], arr[min_id]
    return arr


print(sort(arr))
