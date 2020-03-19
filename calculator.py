from tkinter import *

window = Tk()
window.geometry("400x400")

# --entry field----
entry1 = Entry(width=30, borderwidth=3)
entry1.grid(column=0, row=0, columnspan=3)
window.mainloop()
