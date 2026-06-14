import random


a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]
print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))

isok = False
while not isok:
    try:
        guess = input("input four digits: ")
        if len(guess) != 4:
            raise ValueError("Input must be four digits.")
        else:
            if not guess.isdigit():
               raise ValueError("Input must be numeric.")
        isok = True
    except ValueError as e:
        print("Input error:", e)
