# for i in range(len(arr) - 1):
#     for j in range(len(arr) - 1):
#         if arr[i] + arr[j] == target:
#             print(i, j)
#             break

# target = a+b
# target - a = b
# add in seen
# we check if b in arr: if yes return true/indexes

arr = [1, 3, 4, 5, 6, 7]
target = 9


# Gives you the closed elements
def twosum(arr):
    seen = {}
    for i, num in enumerate(arr):
        sub = target - arr[i]
        if sub in seen:
            return [seen[sub], i]
        seen[num] = i


"""
pass 1:
# hasmap aka dict seen = {empty}
# 0, 1
# cam = 9-1= 8
# No --> #Skip
# Seen = {1 : 0} 

pass 2:
#seen = {1:0}
# 1,3 
# cam = 9-3 = 6 
# No --> Skip 
# seen {1:0, 3:1}

pass3:
# seen {1:0, 6:1}
# 2, 4
# cam = 9-4 = 5
# No --> Skip 
# seen {1:0, 3:1, 4:2}

Pass 4:
# seen {1:0, 3:1, 4:2}
# 3, 5 
# cam = 9-5 = 4 
# Yes --> seen[4], 3 --> 2,3 
# seen {1:0, 3:1, 4:2}
"""


print(twosum(arr))


# will give you farthest elements

print(sorted(arr))


def twosumbinary(arr):
    p, q = 0, len(arr) - 1
    while p <= q:
        s = arr[p] + arr[q]
        if s == target:
            return [p, q]
        elif s < target:
            p += 1
        else:
            q -= 1


print(twosumbinary(arr))
