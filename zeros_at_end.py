arr = [1, 2, 0, 4, 3, 0, 5, 0]

count = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[i], arr[count] = arr[count], arr[i]
        count += 1

print(arr)


# p, q = 0, len(arr) - 1

# while p < q:
#     if arr[p] == 0 and arr[q] != 0:
#         arr[p], arr[q] = arr[q], arr[p]
#         p += 1
#         q -= 1
#     elif arr[p] != 0:
#         p += 1
#     else:
#         q -= 1

# print(arr)
