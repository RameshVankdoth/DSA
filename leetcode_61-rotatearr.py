nums = [1, 2, 3, 4, 5, 6, 7]
k = 3


def rotate(k, nums):
    n = len(nums)

    def rev(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    rev(0, n - 1)
    rev(0, k - 1)
    rev(k, n - 1)

    return nums


print(rotate(k, nums))
