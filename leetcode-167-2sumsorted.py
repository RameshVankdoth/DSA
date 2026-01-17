def twoSum(numbers, target):
    p, q = 0, len(numbers) - 1
    while p < q:
        cam = numbers[p] + numbers[q]
        if cam == target:
            break
        if cam > target:
            q -= 1
        else:
            p += 1
    return [p + 1, q + 1]


numbers = [2, 7, 11, 15]
target = 9

print(twoSum(numbers, target))
