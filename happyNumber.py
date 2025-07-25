def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum([int(n) ** 2 for n in str(num)])
    return n == 1


num = 355

print(isHappy(num))


""" 
An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
Given an integer n, return true if n is an ugly number.
Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors.
"""


def ugly_number(n):
    if n <= 0:
        return False
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False


print(ugly_number(5))
