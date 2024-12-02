import tkinter as tk
from tkinter import ttk  
from calculator import Calculator
from daily_notes import DailyNotes
from quotes_generator import QuotesGenerator
from timer import Timer
from todo_list import TodoList


class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Productivity Toolkit")
        self.master.geometry("850x5000") 
        self.master.resizable(False, False)

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        tabs = [
            ("Calculator", Calculator),
            ("Daily Notes", DailyNotes),
            ("Quotes Generator", QuotesGenerator),
            ("Timer", Timer),
            ("To-Do List", TodoList),
        ]

        for tab_name, TabClass in tabs:
            frame = ttk.Frame(self.notebook) 
            self.notebook.add(frame, text=tab_name)
            TabClass(frame)  


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
