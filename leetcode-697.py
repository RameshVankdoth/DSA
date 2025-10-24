nums = [1, 2, 2, 3, 1, 4, 2]
C = {}
for i, n in enumerate(nums):
    if n in C:
        C[n].append(i)
    else:
        C[n] = [i]
    M = max([len(i) for i in C.values()])
print(min([i[-1] - i[0] for i in C.values() if len(i) == M]) + 1)

# # nums = [1, 2, 2, 3, 1]

# nums = [1, 2, 2, 3, 1, 4, 2]
# p, q = 0, len(nums)
# ans = []
# indexes = {}

# for i in range(0, q):
#     print(f"i is {nums[i]}")
#     for j in range(i + 1, q):
#         print(f"j is {nums[j]}")
#         if nums[i] == nums[j]:
#             indexes[nums[i]] = indexes[nums[i]].value
#             print(nums[i], nums[j])

# for x in indexes.values():
#     ans.append(x[-1] - x[-2] + 1)

# print(min(ans))
