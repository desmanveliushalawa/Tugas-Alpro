import tkinter as tk

class TodoList:
    def __init__(self, master):
        self.master = master
        self.task_listbox = tk.Listbox(master, height=15, width=55, font=("Tmr", 14))
        self.task_listbox.pack(pady=22)

        self.task_entry = tk.Entry(master, font=("Tmr", 14), width=55)
        self.task_entry.pack(pady=12)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(master, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def mark_completed(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, f"{selected_task} (Completed)")
        except IndexError:
            pass  

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            pass  
