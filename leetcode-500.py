keys = {1: "qwertyuiop", 2: "asdfghjkl", 3: "zxcvbnm"}
words = ["Hello", "Alaska", "Dad", "Peace"]


def findWords(words):
    res = []
    for word in words:
        lower = word.lower()
        for key in keys.values():
            if lower[0] in key:
                if all(i in key for i in lower):
                    res.append(lower)
                break
    return res


print(findWords(words))
