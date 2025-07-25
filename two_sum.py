arr = [0, -1, 2, -3, 1]
target = -2

# Two elements in the array who has sum = target

# 1. Naive approach O(n^2)
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(i, j)

# 2. Two pointer approach
arr = sorted(arr)
a = 0
b = len(arr) - 1
while a < b:
    add = arr[a] + arr[b]
    if target == add:
        print(arr[a], arr[b])
        break
    elif add < target:
        a += 1
    else:
        b -= 1

# 3. Hashmap approach
seen = {}
# for i, num in enumerate(arr):
#     comp = target - num
#     if comp in seen:
#         print(seen[comp], i)
#     seen[num] = i
for i in range(len(arr)):
    comp = target - arr[i]
    if comp in seen:
        print(seen[comp], i)
    seen[arr[i]] = i


se = set()
for i in arr:
    comp = target - i
    if comp in se:
        print("True")
    se.add(i)
