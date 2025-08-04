def remove(s):
    # ans = []
    # for i in range(0, len(s)):
    #     if s[i] in ans:
    #         ans.pop(i)
    #         ans.append(s[i])
    #     else:
    #         ans.append(s[i])

    # return "".join(i for i in ans)
    last_occurrence = {ch: i for i, ch in enumerate(s)}
    stack = []
    seen = set()

    for i, ch in enumerate(s):
        if ch not in seen:
            while stack and ch < stack[-1] and i < last_occurrence[stack[-1]]:
                removed = stack.pop()
                seen.remove(removed)
            stack.append(ch)
            seen.add(ch)

    return ''.join(stack)

print(remove("cbacdcbc"))
