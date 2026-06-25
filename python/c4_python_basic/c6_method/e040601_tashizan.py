def tashizan(a, b):
    total = 0
    for i in range(a, b):
        total += i
    return total


c = tashizan(1, 5)
print(c)
c = tashizan(1, 10 + 1)
print(c)
