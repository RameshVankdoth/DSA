arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p, q = 0, len(arr) - 1  # 2 pointers approach

print(arr)
while p < q:
    arr[p], arr[q] = arr[q], arr[p]
    p += 1
    q -= 1

print(arr)  # time = O(n)

arr2 = [32, 1, 4, 7, 85, 47, 86, 78]
print(arr2)
print(arr2[::-1])
