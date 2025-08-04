def look_and_say(n):
    result = "1"
    for _ in range(n - 1):
        current = ""
        i = 0
        while i < len(result):
            count = 1
            while i + 1 < len(result) and result[i] == result[i + 1]:
                count += 1
                i += 1
            current += str(count) + result[i]
            i += 1
        result = current
    ans = reversed(result)
    return ans


# Get the 5th term
print(look_and_say(5))  # Output: 111221


# def countAndSay(n):
#     arr = []
#     ans = ""

#     def helper(arr):

#         return arr

#     if n == 1:
#         arr.append([1, 1])
#         return 1
#     else:
#         return helper(arr)


# n = 1
# print(countAndSay(n))


# def helper(s):
#     pass


# def count(s):
#     ans = {}
#     for i in s:
#         if i in ans:
#             ans[i] += 1
#         else:
#             ans[i] = 1
#     return "".join(str(count) + str(digit) for count, digit in ans.items())


# a = ""
# n = 3
# c = 2
# if n == 1:
#     print("1")
#     a += "1"
# else:
#     while c > 1 and c <= n:
#         b = count(a)
#         a += b
#     print(a)

# # print(count("11253"))
