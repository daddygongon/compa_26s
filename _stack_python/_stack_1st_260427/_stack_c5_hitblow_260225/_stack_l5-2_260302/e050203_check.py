import random

a = random.randint(0,9)
print(a)

b = input("Enter a number between 0 and 9: ")
print("You entered:", b)

if a == int(b):
    print("Congratulations! You guessed the number correctly.")
else:    
    print("Sorry, the correct number was:", a)