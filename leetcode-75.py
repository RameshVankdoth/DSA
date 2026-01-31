nums = [2, 0, 1, 0, 2, 1, 1, 0]
print(nums)

# Can also use the number counting and adding in one array


def printcolor(nums):
    i = 0
    j = len(nums) - 1
    k = 0

    while k <= j:
        if nums[k] == 1:
            k += 1

        elif nums[k] == 2:
            nums[k], nums[j] = nums[j], nums[k]
            j -= 1
        elif nums[k] == 0:
            nums[k], nums[i] = nums[i], nums[k]
            i += 1
            k += 1


# def sortcolor(nums):
#     p, q = 0, 1
#     n = len(nums) - 1
#     while p < q and q <= n:
#         if nums[p] == nums[q]:
#             p += 1
#             q += 1
#             continue
#         elif nums[p] > nums[q]:
#             nums[p], nums[q] = nums[q], nums[p]
#             p += 1
#             q += 1


printcolor(nums)
print(nums)
