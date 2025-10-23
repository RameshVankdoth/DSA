arr = [10, 20, 30, 40, 50]
arr2 = [90, 80, 100, 70, 40, 30]


def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] >= arr[i]:
            return False

    return True
    # return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


print(is_sorted(arr))
print(is_sorted(arr2))
