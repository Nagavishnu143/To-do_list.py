import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


root = tk.Tk()
root.title("To-Do List Application")


def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")


entry = tk.Entry(root, width=30)
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
listbox = tk.Listbox(root, width=50)
scrollbar = tk.Scrollbar(root)


entry.pack(pady=10)
add_button.pack()
delete_button.pack() 
listbox.pack()
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


root.mainloop()
