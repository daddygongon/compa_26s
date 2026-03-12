import random
import tkinter as tk
import tkinter.messagebox as tmsg

def Button1_Clicked():
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
        guess_used = [False]*4
        a_used = [False]*4
        # ヒット判定
        for i in range(4):
            if a[i] == int(guess[i]):
                hit += 1
                guess_used[i] = True
                a_used[i] = True

        # ブロー判定
        blow = 0
        for j in range(4):
            if guess_used[j]:
                continue
            for i in range(4):
                if a_used[i]:
                    continue
                if int(guess[j]) == a[i]:
                    blow += 1
                    a_used[i] = True
                    break

        if hit == 4:
            tmsg.showinfo("Congratulations", "You win!")
            root.destroy()
        else:
            rirekibox.insert(tk.END, "Input: " + guess +",H: " + str(hit)+ ",B: " + str(blow))
            rirekibox.insert(tk.END, "\n")
            rirekibox.see(tk.END)  # 最新行が見えるようにスクロール


a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]
# print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))

root = tk.Tk()
root.geometry("600x400")
root.title("Hit and Blow Game")

rirekibox = tk.Text(root, font = ("Helvetica", 14))
rirekibox.place(x = 350, y = 0, width = 240, height = 400)
# スクロールバーを追加
scrollbar = tk.Scrollbar(root, command=rirekibox.yview)
scrollbar.place(x=590, y=0, height=400)
rirekibox.config(yscrollcommand=scrollbar.set)

label1 = tk.Label(root, text = "Input 4 digits number", font = ("Helvetica", 14))
label1.place(x = 20, y = 20)

editbox1 = tk.Entry(root, width = 4, font = ("Helvetica", 28))
editbox1.place(x = 120, y = 60)
# EnterキーでButton1_Clickedを呼ぶ
editbox1.bind('<Return>', lambda event: Button1_Clicked())

button1 = tk.Button(root, text = "check", font = ("Helvetica", 14),
    command = Button1_Clicked)
button1.place(x = 220, y = 60)

root.mainloop()
