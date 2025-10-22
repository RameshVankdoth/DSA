nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]


def lcseq(nums):
    ans = set(nums)
    long = 0
    for n in ans:
        if n - 1 not in ans:
            l = 1
            while n + l in ans:
                l += 1
            long = max(long, l)
    return long


print(lcseq(nums))
