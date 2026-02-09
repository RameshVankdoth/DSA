arr = [5, 1, 7, 4, 58, 10, 6]


def partition(arr, start, end):
    idx = start - 1
    pivot = arr[end]
    for j in range(start, end):
        if arr[j] < pivot:
            idx += 1
            arr[idx], arr[j] = arr[j], arr[idx]
    idx += 1
    arr[idx], arr[end] = arr[end], arr[idx]
    return idx


def quicksort(arr, start, end):
    if start >= end:
        return
    p = partition(arr, start, end)
    quicksort(arr, start, p - 1)
    quicksort(arr, p + 1, end)


quicksort(arr, 0, len(arr) - 1)
print(arr)
