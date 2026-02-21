s = "A man, a plan, a canal: Panama"


def isValidPalindrome(s):
    s = "".join(c.lower() for c in s if c.isalnum())
    p, q = 0, len(s) - 1
    while p < q:
        if s[p] != s[q]:
            return False
        p += 1
        q -= 1
    return True


print(isValidPalindrome(s))
