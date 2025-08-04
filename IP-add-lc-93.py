def restoreIpAddresses(s):
    if len(s) == 4:
        return ".".join(s[i : i + 1] for i in range(0, len(s), 1))
    else:
        return 1


print(restoreIpAddresses("0000"))
print(restoreIpAddresses("255255255255"))


def generate_substrings(s: str):
    substrings = []
    # Loop to pick the start index
    for i in range(len(s)):
        # Loop to pick the end index
        for j in range(i + 1, len(s) + 1):
            key = s[i:j]
            substrings.append(key)
            # if key == key[::-1]:
            #     substrings.append(s[i:j])
    return substrings


# Example usage
s = "aab"
substrings = generate_substrings(s)
print(substrings)
