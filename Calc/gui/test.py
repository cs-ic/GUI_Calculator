from tkinter import *

root = Tk()

# Creating a label Widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My Name is lalalal")
myLabel3 = Label(root, text=" ")

# Shoving it on screen at any available spot
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)

root.mainloop()
