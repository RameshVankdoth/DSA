a = "abab"
s = "Ramesh Vankdoth Ramesh Vankdoth"

print(set(a))
print(set(s.split(" ")))

print(len(set(a)))
print(len(set(s.split(" "))))


def match(a, s):
    w = s.split()
    hashmap = {}
    for i in range(len(a)):
        if a[i] in hashmap:
            if hashmap[a[i]] != w[i]:
                return False
        else:
            if w[i] in hashmap.values():
                return False
            else:
                hashmap[a[i]] = w[i]
                print(hashmap)
    return True


print(match(a, s))
