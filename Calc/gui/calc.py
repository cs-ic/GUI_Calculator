from tkinter import *

root = Tk()

root.title("Calculator")

e = Entry(root, height=2, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "+":
        e.insert(0, f_num + int(second_number))
    if math == "-":
        e.insert(0, f_num - int(second_number))
    if math == "*":
        e.insert(0, f_num * int(second_number))
    if math == "/":
        e.insert(0, f_num / int(second_number))
    if math == "^":
        e.insert(0, pow(f_num, int(second_number)))
    if math == "%":
        e.insert(0, (int(second_number) / 100))
    if math == "^2":
        e.insert(0, pow(f_num, 2))
    if math == "^3":
        e.insert(0, pow(f_num, 3))


def button_func(operation):
    first_number = e.get()
    global f_num
    global math
    math = operation
    f_num = int(first_number)
    e.delete(0, END)


# button
button_1 = Button(root, text="1", padx=30, pady=5, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=5, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=5, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=5, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=5, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=5, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=5, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=5, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=5, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=5, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=30, pady=5, command=lambda: button_func("+"))
button_sub = Button(root, text="-", padx=30, pady=5, command=lambda: button_func("-"))
button_mul = Button(root, text="*", padx=30, pady=5, command=lambda: button_func("*"))
button_div = Button(root, text="/", padx=30, pady=5, command=lambda: button_func("/"))
button_pow = Button(root, text="^", padx=30, pady=5, command=lambda: button_func("^"))
button_per = Button(root, text="%", padx=30, pady=5, command=lambda: button_func("%"))
button_sqr = Button(
    root, text="x^2", padx=30, pady=5, command=lambda: button_func("^2")
)
button_cub = Button(
    root, text="x^3", padx=30, pady=5, command=lambda: button_func("^3")
)
button_clear = Button(root, text="Clear", padx=18, pady=5, command=button_clear)
button_equal = Button(root, text="=", padx=30, pady=5, command=button_equal)

# Putting button on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_pow.grid(row=1, column=4)
button_per.grid(row=2, column=4)
button_sqr.grid(row=3, column=4)
button_cub.grid(row=4, column=4)

button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1)
button_clear.grid(row=4, column=2)


root.mainloop()
