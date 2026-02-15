decks = [1, 2, 3, 4, 4, 3, 2, 1]

from collections import Counter
from math import gcd


def deckcheck(deck):
    deck.sort()
    counts = list(Counter(deck).values())
    curr_gcd = counts[0]
    for i in counts[1:]:
        curr_gcd = gcd(curr_gcd, i)
    return curr_gcd >= 2

    # deck.sort()
    # if len(deck) < 2:
    #     return False
    # freq = {}
    # for i in deck:
    #     if i in freq:
    #         freq[i] += 1
    #     else:
    #         freq[i] = 1
    # cam = list(freq.values())
    # m = min(cam)
    # for i in range(2, m + 1):
    #     for c in cam:
    #         if c % i != 0:
    #             break
    #     else:
    #         return True

    # return False


print(deckcheck(decks))
