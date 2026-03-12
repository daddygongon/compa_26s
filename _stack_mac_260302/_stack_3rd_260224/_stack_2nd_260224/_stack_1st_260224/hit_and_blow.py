import random

a = random.randint(0, 9)
print(a)

b = int(input("数字を入力してください"))
print(b)

if a == b:
    print("Hit")
else:
    print("Blow")
