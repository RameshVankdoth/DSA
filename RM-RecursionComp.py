# Countdown: Print N down to 1 recursively.
def printf(n):
    if n > 0:
        print(n)
        printf(n - 1)


printf(6)


# Factorial: Calculate n * (n-1)!.
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))


# Sum of N: Calculate n + (n-1) recursively.
def sumofn(n):
    if n <= 0:
        return -1
    return n + sumofn(n - 1)


print(sumofn(5))


# Fibonacci: Calculate the Nth Fibonacci number.
def fibo(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo(n - 1) + fibo(n - 2)


print(fibo(15))


# Print Array: Print array elements index 0 to N recursively.
def printArray(arr, n):
    if n < 0:
        return
    printArray(arr, n - 1)
    print(arr[n])


arr = [1, 2, 3, 4, 5, 6, 8]
printArray(arr, len(arr) - 1)

# Power: Calculate x to the power of n.
x, n = 4, 5


def power(x, n):
    ans = 1
    if x == 1 or n == 0:
        return 1

    return power(x, n - 1) * x


print(power(x, n))


# Count Digits: Recursively divide by 10 to count digits in a number.
def count(n):
    if n // 10 == 0:
        return 1
    return 1 + count(n // 10)


print(count(1234))


# Sum of Digits: Recursively sum the digits of a number (123 -> 6).
def sumofd(n):
    if n == 0:
        return 0
    return (n % 10) + sumofd(n // 10)


print(sumofd(1234456))


# Reverse String: Recursively swap or build a reversed string.
def rev(s, n):
    if n == 0:
        return s[n]
    return s[n] + rev(s, n - 1)


s = "ramesh"
print(rev(s, len(s) - 1))


# GCD: Find the Greatest Common Divisor of two numbers.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(202, 25))
