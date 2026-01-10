arr = [-1, -0, 1, 2, -1, -4]
target = 0
ans = set()
# requirement is arr[i] + arr[j] + arr[k] = target, find the pairs do not repeat the answer array, order of ans array does not matter

# Bruteforce extreme O(n*n*n)

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr) - 1):
        for k in range(j + 1, len(arr) - 1):
            if arr[i] + arr[j] + arr[k] == target:
                cam = [arr[i], arr[j], arr[k]]
                cam.sort()
                ans.add(tuple(cam))

print(ans)
