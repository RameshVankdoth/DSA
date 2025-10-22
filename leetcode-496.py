def nextGreaterElement(nums1, nums2):
    # stack = []
    # hashmap = {}
    # for num in nums2:
    #     while stack and num > stack[-1]:
    #         hashmap[stack.pop()] = num
    #     stack.append(num)
    # return [hashmap.get(i, -1) for i in nums1]
    ans = []
    for key in nums1:
        idx = nums2.index(key)
        next_greater = -1
        for j in range(idx + 1, len(nums2)):
            if nums2[j] > key:
                next_greater = nums2[j]
                break
        ans.append(next_greater)
    return ans


nums1 = [4, 1, 2]
nums2 = [1, 2, 3, 4]
print(nextGreaterElement(nums1, nums2))
