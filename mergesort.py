arr = [1, 7, 2, 45, 24, 12, 5, 10]

# 97 122 - Lower
# 65 92 - Capital 

def merge(l, r):
    ans = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            ans.append(l[i])
            i += 1
        else:
            ans.append(r[j])
            j += 1
    ans.extend(l[i:])
    ans.extend(r[j:])
    return ans


def divide(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    l = divide(left)
    r = divide(right)
    return merge(l, r)


print(divide(arr))
