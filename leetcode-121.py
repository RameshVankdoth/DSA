arr = [7, 4, 5, 6, 3, 1, 9]


def best_time(arr):
    bp = arr[0]
    profit = 0
    for i in arr[1:]:
        if i < bp:
            bp = i
        profit = max(profit, i - bp)

    return profit


print(best_time(arr))
