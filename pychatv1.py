from tkinter import *

win = Tk()
win.title("pychat")
win.geometry("1000x1000+50+50")
win.config(bg="skyblue")

leftPane = Frame(win, width=400, height=400, bg="grey")
leftPane.grid(row=0, column=1, padx=5, pady=5)

rightPane = Frame(win, width=200, height=200, bg="yellow")
rightPane.grid(row=0, column=2, padx=10, pady=10)

win.mainloop()
