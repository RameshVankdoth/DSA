s = "leetcode"
wordDict = ["leet", "code"]


def word(s, wordDict):
    # ans = False
    # for i in w:
    #     x = len(i)
    #     m = 0
    #     while m < x and s[m] == i[m]:
    #         m += 1
    #         ans = True
    # return ans
    # ans = []
    # for i in w:
    #     if s.find(i):
    #         ans.append(True)
    #     else:
    #         ans.append(False)
    # return ans[-1]

    dp = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        for w in wordDict:
            start = i - len(w)
            if start >= 0 and dp[start] and s[start:i] == w:
                dp[i] = True
                break

        return dp[-1]


print(word(s, wordDict))
