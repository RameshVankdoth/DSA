def addBinary(a, b):
    carry = 0
    result = []
    p, q = len(a) - 1, len(b) - 1
    while p >= 0 or q >= 0 or carry:
        x = int(a[p]) if p >= 0 else 0
        y = int(b[q]) if q >= 0 else 0
        add = x + y + carry
        digit = add % 2
        carry = add // 2
        result.append(str(digit))
        p -= 1
        q -= 1
    return "".join(result[::-1])


print(addBinary("11", "1"))

print(bin(int("1101", 2) + int("1000", 2))[2:])
