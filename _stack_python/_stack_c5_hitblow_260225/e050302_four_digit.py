import random

a1 = random.randint(0, 9)
a2 = random.randint(0, 9)
a3 = random.randint(0, 9)
a4 = random.randint(0, 9)

print(str(a1) + str(a2) + str(a3) + str(a4))

a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]
print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))
# copilot suggestion
a = [random.randint(0, 9) for _ in range(4)]
print(''.join(str(x) for x in a))
