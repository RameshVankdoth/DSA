def lemonadeChange(bills):
    money = {5: 0, 10: 0, 20: 0}
    for i in bills:
        if i == 5:
            money[5] += 1
        elif i == 10:
            if money[5] > 0:
                money[5] -= 1
                money[10] += 1
            else:
                print("Failed in 10", money, "and", bills)
                return money
        elif i == 20:
            if money[10] > 0 and money[5] > 0:
                money[10] -= 1
                money[5] -= 1
            elif money[5] >= 3:
                money[5] -= 3
            else:
                print("Failed in 20", money, "and", bills)
                return money
            money[20] += 1
    return money


nums = [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]
print(lemonadeChange(nums))
