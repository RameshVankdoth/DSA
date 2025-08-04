words = ["cd", "ac", "dc", "ca", "zz"]
rev = {}
count = 0

for i in range(len(words)):
    if words[i] in rev.values():
        count += 1
    rev[i] = words[i][::-1]

print(rev)
print(count)
