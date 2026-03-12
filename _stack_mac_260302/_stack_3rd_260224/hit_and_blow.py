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

hit = 0
for i in range(4):
    if a[i] == int(b[i]):
        hit += 1

blow = 0
for j in range(4):
    for k in range(4):
        if a[j] == int(b[k]) and a[j] != int(b[j]):
            blow += 1

print("Hit: " + str(hit))
print("Blow: " + str(blow))
