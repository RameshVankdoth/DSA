def judgeSquareSum(c):
    q = int(c**0.5)
    p = 0
    while p <= q:
        cal = p**2 + q**2
        if cal == c:
            return True
        elif cal > c:
            q -= 1
        else:
            p += 1
    return False


print(judgeSquareSum(5))
