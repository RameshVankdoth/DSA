arr = [15, 2, 6, 10, 23, 18, 6, 30, 50, 4, 90]


# def sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i
#         while j > 0 and arr[j - 1] > key:
#             arr[j] = arr[j - 1]
#             j -= 1
#         arr[j] = key
#     return arr


# print(sort(arr))


def sort(arr):
    for i in range(len(arr)):
        j = i
        key = arr[i]
        while j > 0 and arr[j - 1] > key:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = key
    return arr


print(sort(arr))
