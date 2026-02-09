from BinarySearch import Binary

nums = [4, 5, 6, 7, 0, 1, 2]
nums2 = [7, 0, 1, 2, 4, 5, 6]
target = 0

# arr, rotated --> sorted --> 3 rotate
# find the target == 0

# nums = [4, 5, 6, 7 -- binary
# nums2 = 0, -- mid
# nums3 = 1, 2] -- binary


def rotatedbinary(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


print(rotatedbinary(nums, target))
