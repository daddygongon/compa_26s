import tkinter as tk

root = tk.Tk()
root.geometry("400x150")
root.title("Hit and Blow Game")

label1 = tk.Label(root, text = "Input 4 digits number", font = ("Arial", 14))
label1.place(x = 20, y = 20)

editbox1 = tk.Entry(root, width = 4, font = ("Arial", 28))
editbox1.place(x = 120, y = 60)

button1 = tk.Button(root, text = "check", font = ("Arial", 14))
button1.place(x = 220, y = 60)

root.mainloop()