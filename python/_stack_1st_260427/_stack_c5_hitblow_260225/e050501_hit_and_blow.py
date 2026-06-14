import random


a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]
print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))

while True:
    isok = False
    while isok == False:
        guess = input("input four digits: ")
        if len(guess) != 4:
            print("Input error: Input must be four digits.")
        else:
            kazuok = True
            for i in range(4):
                if guess[i] < '0' or guess[i] > '9':
                    print("Input error: Input must be numeric.")
                    kazuok = False
                    break
            if kazuok:
                isok = True
    print("Your input is: " + guess)

    hit = 0
    for i in range(4):
        if a[i] == int(guess[i]):
            hit += 1

    print("Hit: " + str(hit))

    blow = 0
    for j in range(4):
        for i in range(4):
            if (int(guess[j]) == a[i]) and (a[i] != int(guess[i])):
                blow += 1
                break
    print("Blow: " + str(blow))

    if hit == 4:
        print("Congratulations! You win!")
        break