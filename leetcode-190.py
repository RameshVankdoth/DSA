# n = 43261596
# binary = bin(n)[2:]
# print("00000010100101000001111010011100")
# print(binary)
# b = [int(i) for i in binary]
# k = len(b)
# l, r = 0, k - 1

# # while l < r:
# #     b[l], b[r] = b[r], b[l]
# #     l += 1
# #     r -= 1

# result = "".join(str(i) for i in b)

# print(result)

# decimal = 0
# for i in range(k - 1, -1, -1):
#     decimal += int(b[i]) * 2**i

# print(decimal)

n = 43261596
binary = format(n, "032b")
print(binary)

reversed_binary = binary[::-1]
print(int(reversed_binary, 2))
