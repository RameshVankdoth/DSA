a = [12,244,346,234,1,67,325,78,567]
m1, m2 = float('-inf'), float('-inf')

for i in range(len(a)):
    if a[i] > m1 and a[i] < m2:
        m1 = a[i]
    elif a[i] > m2:
        m1 = m2
        m2 = a[i]
print(m1)