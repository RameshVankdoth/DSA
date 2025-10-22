nums = [4, 3, 2, 7, 8, 2, 3, 1]


def findDisappearedNumbers(nums):
    n = len(nums)
    for i in range(n):

        while nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            # print(nums[nums[i] - 1], "and", nums[i])
    return [i + 1 for i in range(n) if nums[i] != i + 1]


print(findDisappearedNumbers(nums))
