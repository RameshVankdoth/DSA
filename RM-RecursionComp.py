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
# def printArray(arr):
#     if len(arr) == 1:
#         print(arr[0])
#     elif not arr:
#         print(0)
#     else:
#         print(arr[printArray(arr)])

# Power: Calculate x to the power of n.

# Count Digits: Recursively divide by 10 to count digits in a number.

# Sum of Digits: Recursively sum the digits of a number (123 -> 6).

# Reverse String: Recursively swap or build a reversed string.

# GCD: Find the Greatest Common Divisor of two numbers.
