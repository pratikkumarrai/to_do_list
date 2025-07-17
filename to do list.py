import tkinter as tk
from tkinter import messagebox, font

# Add a task to the list
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Delete selected task
def delete_task():
    try:
        selected = listbox_tasks.curselection()
        listbox_tasks.delete(selected)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Cross out a task (mark as completed)
def cross_task():
    try:
        selected = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected)
        if not task.startswith("✔️ "):
            listbox_tasks.delete(selected)
            listbox_tasks.insert(selected, "✔️ " + task)
            listbox_tasks.itemconfig(selected, fg="gray", font=crossed_font)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to cross out.")

# Uncross a task (mark as incomplete)
def uncross_task():
    try:
        selected = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected)
        if task.startswith("✔️ "):
            new_task = task.replace("✔️ ", "", 1)
            listbox_tasks.delete(selected)
            listbox_tasks.insert(selected, new_task)
            listbox_tasks.itemconfig(selected, fg="black", font=normal_font)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to uncross.")

# Create main window
root = tk.Tk()
root.title("Blue To-Do List")
root.geometry("450x500")
root.configure(bg="#B3D1FF")  # light blue background
root.resizable(False, False)

# Fonts
normal_font = font.Font(family="Arial", size=12)
crossed_font = font.Font(family="Arial", size=12, overstrike=1)

# Entry for task
entry_task = tk.Entry(root, font=normal_font, width=30, bg="#E6F0FF")
entry_task.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#B3D1FF")
btn_frame.pack()

btn_add = tk.Button(btn_frame, text="Add Task", width=15, command=add_task, bg="#80BFFF", fg="white")
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_delete = tk.Button(btn_frame, text="Delete Task", width=15, command=delete_task, bg="#FF6666", fg="white")
btn_delete.grid(row=0, column=1, padx=5, pady=5)

btn_cross = tk.Button(btn_frame, text="Cross Out", width=15, command=cross_task, bg="#4DA6FF", fg="white")
btn_cross.grid(row=1, column=0, padx=5, pady=5)

btn_uncross = tk.Button(btn_frame, text="Uncross", width=15, command=uncross_task, bg="#4DA6FF", fg="white")
btn_uncross.grid(row=1, column=1, padx=5, pady=5)

# Task list
listbox_tasks = tk.Listbox(root, width=40, height=15, font=normal_font, selectbackground="#99CCFF")
listbox_tasks.pack(pady=10)

# Start GUI loop
root.mainloop()

