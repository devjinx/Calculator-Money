from tkinter import *
from tkinter import ttk

root = Tk()
root.title("คำนวณการเก็บเงินภายใน 1 ปี")

#input
Label(text="จำนวนเงินที่คุณต้องการเก็บ", padx=10, font=30).grid(row=0, sticky=W)
money = IntVar()
et1=Entry(font=30,width=30, textvariable=money)
et1.grid(row=0, column=1)

#output
Label(text="คุณควรเก็บเงิน", padx=10, font=30).grid(row=2, sticky=W)
et2=Entry(font=30,width=30)
et2.grid(row=2, column=1)
def calculate():
    m = money.get()
    m1 = m / 12
    et2.insert(0,m1)

Button(text="คำนวณ", font=30,width=15, command=calculate).grid(row=3, column=1, sticky=W)

root.geometry("500x500")
root.mainloop()