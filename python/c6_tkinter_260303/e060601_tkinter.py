import random
import tkinter as tk
import tkinter.messagebox as tmsg

def Button1_Clicked():
    print("Button1 was clicked")
    guess = editbox1.get()

    isok = False
    if len(guess) != 4:
        tmsg.showerror("Input Error", "Input must be four digits.")
    else:
        kazuok = True
        for i in range(4):
            if guess[i] < '0' or guess[i] > '9':
                tmsg.showerror("Input Error", "Input must be numeric.")
                kazuok = False
                break
        if kazuok:
            isok = True
    
    if isok:
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
            tmsg.showinfo("Congratulations", "You win!")
            root.destroy()
        else:
            rirekibox.insert(tk.END, "Input: " + guess +",H: " + str(hit)+ ",B: " + str(blow) + "\n")


a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]
print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))

root = tk.Tk()
root.geometry("600x400")
root.title("Hit and Blow Game")

rirekibox = tk.Text(root, font = ("Helvetica", 14))
rirekibox.place(x = 400, y = 0, width = 200, height = 400)

label1 = tk.Label(root, text = "Input 4 digits number", font = ("Helvetica", 14))
label1.place(x = 20, y = 20)

editbox1 = tk.Entry(root, width = 4, font = ("Helvetica", 28))
editbox1.place(x = 120, y = 60)

button1 = tk.Button(root, text = "check", font = ("Helvetica", 14),
    command = Button1_Clicked)
button1.place(x = 220, y = 60)

root.mainloop()