haystack = "sadbutsad"
needle = "helo"

# print(haystack.find(needle))

haystack = "sadbutsad"
needle = "sad"

found = False
for i in range(len(haystack) - len(needle) + 1):
    if haystack[i : i + len(needle)] == needle:
        print(i)
        found = True
        break

if not found:
    print(-1)
