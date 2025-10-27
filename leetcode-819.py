# from collections import Counter

# # def mostCommonWord(paragraph, banned):
# #     track = {}
# #     for i in paragraph.split():
# #         print(i.lower())
# #         key = i.lower()
# #         if key in track:
# #             track[key] += 1
# #         else:
# #             track[key] = 1
# #     return track
# #     # for i in track:
# #     #     if


# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# paragraph = set(paragraph.split())
# banned = ["hit"]

# # ans = Counter.most_common(paragraph)
# print(paragraph)
# # print(ans)

# # print(mostCommonWord(paragraph, banned))

a = [1, 2, 1, 3, 4, 5, 5, 6]
banned = [1]
track = {}
for i in a:
    if i in track:
        track[i] += 1
    else:
        track[i] = 1
print(track)

curr_re = 0
ans = 0
for a, b in track.items():
    if a not in banned and curr_re < b:
        curr_re = b
        ans = a
print(ans)

# listval = [[a, b] for a, b in track.items()]
# print(listval)
