arr = [10, 15, 2, 4, 60, 3, 25, 80, 12, 13]
n = len(arr)


def merge(left, right):
    ans = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1

    ans.extend(left[i:])
    ans.extend(right[j:])
    return ans


def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    right = arr[mid:]
    left = arr[:mid]

    righthalf = mergesort(right)
    lefthalf = mergesort(left)

    return merge(lefthalf, righthalf)


print(mergesort(arr))
