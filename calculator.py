from tkinter import *

window = Tk()
# window.geometry("400x400")

# --functions---


def button_click(number):
    if number == 100:
        entry1.delete(0, END)
    elif number == 101:
        global first_num
        first_num = int(entry1.get())
        entry1.delete(0, END)
    elif number == 102:
        second_num = int(entry1.get())
        addition = first_num+second_num
        entry1.delete(0, END)
        entry1.insert(0, str(addition))

    else:
        current = entry1.get()
        entry1.delete(0, END)
        entry1.insert(0, str(current)+str(number))


# --entry field----
entry1 = Entry(width=30, borderwidth=3)
entry1.grid(column=0, row=0, columnspan=3)


# --buttons---

button1 = Button(text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(text="+", padx=40, pady=20,
                    command=lambda: button_click(101))
button_equal = Button(text="=", padx=89, pady=20,
                      command=lambda: button_click(102))
button_clear = Button(text="clear", padx=89, pady=20,
                      command=lambda: button_click(100))


button1.grid(column=0, row=1)
button2.grid(column=1, row=1)
button3.grid(column=2, row=1)

button4.grid(column=0, row=2)
button5.grid(column=1, row=2)
button6.grid(column=2, row=2)

button7.grid(column=0, row=3)
button8.grid(column=1, row=3)
button9.grid(column=2, row=3)

button0.grid(column=0, row=4)
button_add.grid(column=0, row=5)

button_clear.grid(column=1, row=4, columnspan=2)
button_equal.grid(column=1, row=5, columnspan=2)

window.mainloop()
