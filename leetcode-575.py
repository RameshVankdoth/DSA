def distributeCandies(candyType):
    hash = set(candyType)
    n = len(candyType)
    return min(len(hash), n // 2)


candyType = [1, 1, 2, 2, 3]
print(distributeCandies(candyType))
