for a in range(1, 20 + 1):
    print(a, end=" ")
    if a % 12 == 0:
        print("⚪︎")
    elif a % 4 == 0:
        print("△")
    elif a % 2 == 0:
        print("×")
    else:
        print("＊")
