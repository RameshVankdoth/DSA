timeSeries = [1, 2, 3, 4, 5, 6, 7, 8, 9]
duration = 10000


# Brute force solution
def findPoisonedDuration(timeSeries, duration):
    sol = []
    n = len(timeSeries)
    for i in range(n):
        key = timeSeries[i]
        key2 = timeSeries[i] + duration - 1
        for j in range(key, key2 + 1, 1):
            sol.append(j)
        print(sol)

    return len(set(sol))


print(findPoisonedDuration(timeSeries, duration))


# optimied solution
def findPoisonedDuration2(timeSeries, duration):
    ans = 0

    for i in range(len(timeSeries) - 1):
        if timeSeries[i] + duration > timeSeries[i + 1]:
            ans += timeSeries[i + 1] - timeSeries[i]
        else:
            ans += duration

    return ans + duration


print(findPoisonedDuration2(timeSeries, duration))
