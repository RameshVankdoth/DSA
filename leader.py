# Input: arr[] = [16, 17, 4, 3, 5, 2]
# Output: [17 5 2]

# Naive approach O(n2) and O(1)

arr = [16, 17, 4, 3, 5, 2]
ans = []

for i in range(len(arr)):
    key = arr[i]
    for j in range(i + 1, len(arr)):
        if arr[j] > key:
            break
    else:
        ans.append(arr[i])

print(ans)


# optimal approach O(n) and  O(1)
arr = [16, 17, 4, 3, 5, 2]
ans2 = []
maxr = arr[-1]
ans2.append(maxr)
for i in range(len(arr) - 2, -1, -1):
    if arr[i] >= maxr:
        maxr = arr[i]
        ans2.append(maxr)
ans2.reverse()
print(ans2)
