# import math

n = 3


# def inPrime(n):
#     res = []
#     if n <= 0:
#         return 0
#     for j in range(n):
#         for i in range(2, int(math.sqrt(j)) + 1):
#             if j % i == 0:
#                 res.append(j)
#     return res


# print(inPrime(n))


def isprime(n):
    if n <= 2:
        return 0
    prime = [True] * n
    prime[0], prime[1] = False, False
    p = 2
    while p * p <= n:
        if prime[p]:
            for j in range(p * p, 5 * 10**6, p):
                prime[j] = False

        p += 1
    return sum(prime)


n = 3
print(isprime(n))
