# Input: arr[] = [2, 2, 2, 2, 2]
# Output: [2]
# Explanation: All the elements are 2, So only keep one instance of 2.
arr = [2, 2, 2, 2, 2]
arr2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]


# Using hashmap O(n), O(n)
def remove_hash(arr):
    hashmap = set()
    for i in arr:
        if i not in hashmap:
            hashmap.add(i)
    print(hashmap)


# without hashmap O(n), O(1)
def remove_place(arr):
    n = len(arr)
    idx = 1

    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1
    print(arr)
    print(arr[:idx])


remove_hash(arr)
remove_hash(arr2)
remove_place(arr)
remove_place(arr2)
