arr = [1, 2, 3]


def next_perm(arr):
    n = len(arr)
    i = n - 2
    # while i >= 0 and arr[i] <= arr[i + 1]: Last permutation
    while i >= 0 and arr[i] >= arr[i + 1]:  # Just next permutation
        i -= 1

    if i >= 0:
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]

    l, r = i + 1, n - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        r -= 1
        l += 1

    return arr


print(next_perm(arr))
