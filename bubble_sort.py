arr = [1, 5, 6, 3, 4, 10, 23, 52, 1, 6, 40]
arr2 = [1, 5, 2, 8, 3, 34, 22, 15, 47, 99]
# selection sort
for i in range(len(arr)):
    min_id = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_id]:
            min_id = j
    arr[i], arr[min_id] = arr[min_id], arr[i]

print(arr)

# Bubble sort
for i in range(len(arr2)):
    for j in range(len(arr2) - i - 1):
        if arr2[j] > arr2[j + 1]:
            arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
print(arr2)


# Binary search
def binary(arr, target):
    p, q = 0, len(arr) - 1
    while p <= q:
        mid = p + (q - p) // 2
        if target == arr[mid]:
            return True

        elif target > arr[mid]:
            p = mid + 1
        else:
            q = mid - 1

    return False


print(binary(arr, 4))


# Binary search rotated
rotated = [4, 5, 6, 7, 0, 1, 2, 3]


def bin(arr, target):
    p, q = 0, len(rotated) - 1

    while p <= q:
        mid = p + (q - p) // 2
        if arr[mid] == target:
            return mid
        elif arr[p] <= arr[mid]:
            if arr[p] <= target < arr[mid]:
                q = mid - 1
            else:
                p = mid + 1
        else:
            if arr[mid] < target <= arr[q]:
                p = mid + 1
            else:
                q = mid - 1
    return -1


print(bin(rotated, 5))
