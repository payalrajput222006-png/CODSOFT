import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.config(bg="#1A1A2E")  # Deep navy background

tasks = []

# Functions
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        tasks.append(task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def mark_complete():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(tk.END, "✔️ " + task)
        listbox.itemconfig(tk.END, fg="#00D4AA")  # Teal color for completed tasks
    except:
        messagebox.showwarning("Warning", "Select a task!")

# Title
title = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="#1A1A2E", fg="#E94560")
title.pack(pady=10)

# Entry box
entry = tk.Entry(root, width=25, font=("Arial", 14), bg="#16213E", fg="white", insertbackground="white", relief="flat")
entry.pack(pady=10, ipady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#1A1A2E")
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Task", bg="#E94560", fg="white", width=10, relief="flat", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

del_btn = tk.Button(btn_frame, text="Delete", bg="#F5A623", fg="white", width=10, relief="flat", command=delete_task)
del_btn.grid(row=0, column=1, padx=5)

complete_btn = tk.Button(btn_frame, text="Complete", bg="#00D4AA", fg="white", width=10, relief="flat", command=mark_complete)
complete_btn.grid(row=0, column=2, padx=5)

# Listbox
listbox = tk.Listbox(root, width=30, height=15, font=("Arial", 12), bg="#16213E", fg="white", selectbackground="#E94560", relief="flat", borderwidth=0)
listbox.pack(pady=10)

# Run app
root.mainloop()