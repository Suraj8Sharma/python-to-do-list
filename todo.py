import tkinter as tk
from tkinter import messagebox

# Your logic class, unchanged.
class TodoList:
    """
    Manages the core logic of the to-do list.
    """
    def __init__(self):
        """
        Initializes the to-do list with an empty list of tasks.
        """
        self.tasks = []

    def add_task(self, task_description):
        """
        Adds a new task to the list.
        """
        if task_description:
            self.tasks.append(task_description)
            # The print statements will show up in the terminal when you run the app
            print(f"✅ Added task: '{task_description}'")
        else:
            print("⚠️ Error: Task description cannot be empty.")

    def delete_task(self, task_number):
        """
        Deletes a task from the list by its 1-based number.
        """
        index = task_number - 1
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"🗑️ Deleted task: '{removed_task}'")
        else:
            print("⚠️ Error: Invalid task number. Please try again.")

# --- GUI Functions ---
def update_listbox():
    """This function updates the visual listbox with the tasks from your logic."""
    listbox_tasks.delete(0, tk.END)
    for task in todo_logic.tasks:
        listbox_tasks.insert(tk.END, task)

def add_task_command():
    """This function is called when the 'Add Task' button is clicked."""
    task_description = entry_task.get()
    # We add a check here to avoid calling the logic with an empty string
    if task_description:
        todo_logic.add_task(task_description)
        update_listbox()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task_command():
    """This function is called when the 'Delete Task' button is clicked."""
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        # Your delete_task method expects a 1-based number, so we add 1.
        todo_logic.delete_task(selected_task_index + 1)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# --- Main Application Setup ---

# 1. Create an instance of your logic class
todo_logic = TodoList()

# 2. Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")
root.configure(bg="#2e2e2e") # Dark background for the main window

# 3. Create the GUI Elements (Widgets) with new styling
# Title Label
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#2e2e2e", fg="#ffffff")
title_label.pack(pady=10)

# Frame for listbox and scrollbar
frame_tasks = tk.Frame(root, bg="#2e2e2e")
frame_tasks.pack(pady=10)

# Listbox with dark theme
listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, bg="#404040", fg="#ffffff", selectbackground="#555555", font=("Helvetica", 12), border=0)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

# Scrollbar with dark theme
scrollbar_tasks = tk.Scrollbar(frame_tasks, bg="#404040")
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Entry box with dark theme
entry_task = tk.Entry(root, width=45, bg="#404040", fg="#ffffff", font=("Helvetica", 12), insertbackground="#ffffff", border=0)
entry_task.pack(pady=20)

# Frame for the buttons
button_frame = tk.Frame(root, bg="#2e2e2e")
button_frame.pack(pady=10)

# 'Add Task' button with modern styling
button_add_task = tk.Button(button_frame, text="Add Task", width=15, command=add_task_command, bg="#4a90e2", fg="#ffffff", font=("Helvetica", 10, "bold"), border=0, activebackground="#357ABD")
button_add_task.pack(side=tk.LEFT, padx=10)

# 'Delete Task' button with modern styling
button_delete_task = tk.Button(button_frame, text="Delete Task", width=15, command=delete_task_command, bg="#e24a4a", fg="#ffffff", font=("Helvetica", 10, "bold"), border=0, activebackground="#C13C3C")
button_delete_task.pack(side=tk.LEFT, padx=10)


# 4. Start the application's main loop
root.mainloop()
