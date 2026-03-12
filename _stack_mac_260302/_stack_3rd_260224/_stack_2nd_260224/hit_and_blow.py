import random

a = [
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9),
]
print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))

isok = False
while isok == False:
    b = input("数字を入力してください")
    if len(b) != 4:
        print("4桁の数字を入力してください")
    else:
        kazuok = True
        for i in range(4):
            if b[i] < "0" or b[i] > "9":
                print("数字を入力してください")
                kazuok = False
        if kazuok:
            isok = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])


if a == b:
    print("Hit")
else:
    print("Blow")
