nums = [-1, 0, 1, 2, -1, -4]
target = 0


def threeSum(nums, target):
    if len(nums) <= 1:
        return
    ans = set()
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j, k = i + 1, len(nums) - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total > target:
                k -= 1
            elif total < target:
                j += 1
            else:
                ans.add(tuple([nums[i], nums[j], nums[k]]))
                j += 1
                k -= 1
    return list(ans)

    # ans = set()
    # nums.sort()
    # for i in range(len(nums)):
    #     if i > 0 and nums[i] == nums[i - 1]:
    #         continue
    #     j = i + 1
    #     k = len(nums) - 1
    #     while j < k:
    #         total = nums[i] + nums[j] + nums[k]

    #         if total > target:
    #             k -= 1
    #         elif total < target:
    #             j += 1
    #         else:
    #             ans.add((nums[i], nums[j], nums[k]))
    #             j += 1
    #             while nums[j] == nums[j - 1] and j < k:
    #                 j += 1
    # return ans


print(threeSum(nums, target))
