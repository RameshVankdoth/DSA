from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group(strs):
    ans = defaultdict(list)
    for i in strs:
        sw = "".join(sorted(i))
        ans[sw].append(i)
    return list(ans.values())


print(group(strs))
