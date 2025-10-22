def max_num(nums):
    nums = sorted(nums)
    print(nums)
    ma = 0
    print(ma)
    for i in range(len(nums)):
        ans = "".join(str(i) for i in nums)
        for j in range(i, len(nums)):
            if nums[j] > nums[i]:
                key = "".join(str(i) for i in nums)
                nums[j], nums[i] = nums[i], nums[j]
                print(f"Ans is:{ans} and key is: {key}")
            else:
                continue
            ma = max(ans, key)
    return str(ma)


print(max_num([3, 5, 9, 34, 30]))
