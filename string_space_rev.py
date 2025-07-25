"""Problem is reverse a string with spaces included while their spaces are kept at their original positions"""

# String reversal
s = "I am Ramesh"
s2 = "".join(s[i] for i in range(len(s) - 1, -1, -1))
print(s2)


# Approach Solution
def rev(s):
    left = 0
    s = list(s)
    right = len(s) - 1

    while left < right:
        if s[left] == " ":
            left += 1
            continue

        elif s[right] == " ":
            right -= 1
            continue

        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return "".join(s)


print(rev(s))
