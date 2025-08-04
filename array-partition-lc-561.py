# def arrayPairSum(nums):
#     nums = sorted(nums)
#     sum1 = 0
#     pairs = [
#         [nums[i], nums[j]] for i in range(len(nums)) for j in range(i + 1, len(nums))
#     ]
#     adds = []
#     print(pairs)
#     p, q = 0, len(pairs) - 1
#     while p <= q:
#         sum1 += min(pairs[p]) + min(pairs[q])
#         adds.append(sum1)
#         print("For the pair:", pairs[p], "and", pairs[q])
#         p += 1
#         q -= 1
#         sum1 = 0
#     print(adds)
#     return max(adds)


# arr = [1, 2, 3, 4]
# arr2 = [6, 2, 6, 5, 1, 2]
# print(arrayPairSum(arr))
# print(arrayPairSum(arr2))


def arrayPairSum(nums):
    nums.sort()
    sum1 = 0
    for i in range(0, len(nums), 2):
        sum1 += nums[i]

    return sum1


arr = [1, 2, 3, 4]
arr2 = [6, 2, 6, 5, 1, 2]
print(arrayPairSum(arr))
print(arrayPairSum(arr2))
