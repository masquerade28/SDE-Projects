import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from customtkinter import filedialog
import os

num = 0
def number():
    global num
    num += 1
    return num

def add_todo(todo):
    i=number()
    label = ctk.CTkLabel(scrollable_frame, text=str(i)+"] "+ todo, font=ctk.CTkFont(family="Comic Sans MS"))
    label.pack(anchor = "nw")

    with open("Todo.txt", "a") as file:
        notes = entry.get()
        file.write(str(i)+"] "+ notes +"\n")
        
    entry.delete(0, ctk.END)
   

def clear_todo():

    for label in scrollable_frame.winfo_children():
        label.destroy()
    file = open("Todo.txt", "w")

def load():

    try:
        with open("Todo.txt", "r") as file:
            data = file.readlines()
            for task in data:
                label = ctk.CTkLabel(scrollable_frame, text=task, font=ctk.CTkFont(family="Comic Sans MS"))
                label.pack(anchor = "nw")

    except FileNotFoundError:
        pass

root = ctk.CTk()
root.geometry("750x450")
root.title("Todo App")
root.iconbitmap('Icon.ico')

# Creating Main Title Label
title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(family="Comic Sans MS", size=30, weight="bold"))
title_label.pack(padx=10, pady=(40,10))

# Adding Input Box
entry = ctk.CTkEntry(root, placeholder_text="Press Enter To Add Todo", width=500)
entry.pack(pady=20)

# Creating Scrollable Frame For Todo List
scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
scrollable_frame.pack()

# Adding Button To Clear Data
clear_button = ctk.CTkButton(root, text="Clear", width=250, command=clear_todo)
clear_button.place(relx=0.5, rely=0.95, anchor='s')

# Using Enter Key To Take Input
entry.bind('<Return>', (lambda event: add_todo(entry.get())))
load()
root.mainloop()
