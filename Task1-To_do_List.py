'''TASK 1
A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. 
This project aims to create a command-line or GUI-based application using Python, allowing users to create, 
update, and track their to-do lists'''
from tkinter import *
top = Tk()
datas = []
Task = StringVar()

def add():
    global datas
    datas.append([txname.get()])
    update_book()
    Task.set('')

def update():
    if ls.curselection():
        index = int(ls.curselection()[0])
        datas[index] = [txname.get()]
        update_book()

def delete():
    if ls.curselection():
        del datas[int(ls.curselection()[0])]
        update_book()

def update_book():
    ls.delete(0, END)
    for n in datas:
        ls.insert(END, n[0])

heading = Label(top, text="TO-DO List", font="Arial 12 bold")
heading.grid(row=0, column=2, columnspan=1, padx=10, pady=10)
label = Label(top, text="Task", font="Arial 12 bold")
label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
txname = Entry(top, width=50, textvariable=Task)
txname.grid(row=1, column=2, padx=10, pady=5)
ls = Listbox(top, height=10, width=30)
ls.grid(row=2, column=2, padx=10, pady=5, sticky="nsew", columnspan=2)
scroll_bar = Scrollbar(top, orient=VERTICAL, command=ls.yview)
scroll_bar.grid(row=2, column=3, padx=(0, 10), pady=5, sticky="ns")
ls.config(yscrollcommand=scroll_bar.set)
frame = Frame(top)
butadd = Button(frame, text="Add", command=add, width=10)
butview = Button(frame, text="Update", command=update, width=10)
butdel = Button(frame, text="Delete", command=delete,width=10)
butadd.grid(row=0, column=0, padx=5, pady=5)
butview.grid(row=1, column=0, padx=5, pady=5)
butdel.grid(row=2, column=0, padx=5, pady=5)
frame.grid(row=2, column=1, padx=(10, 0), pady=5)
top.mainloop()
