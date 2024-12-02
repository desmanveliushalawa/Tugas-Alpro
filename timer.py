import tkinter as tk
import time
import threading

class Timer:
    def __init__(self, master):
        self.master = master

        self.timer_label = tk.Label(master, text="00:00", font=("Tmr", 30))
        self.timer_label.pack(pady=22)

        self.start_button = tk.Button(master, text="Start Timer", command=self.start_timer)
        self.start_button.pack(pady=12)

        self.duration_entry = tk.Entry(master, font=("Tmr", 14), width=12)
        self.duration_entry.pack(pady=10)
        self.duration_entry.insert(0, "25")  

    def start_timer(self):
        try:
            duration = int(self.duration_entry.get()) * 60 
            self.start_button.config(state=tk.DISABLED)
            self.countdown(duration)
        except ValueError:
            self.timer_label.config(text="Invalid Input!")

    def countdown(self, remaining_time):
        if remaining_time >= 0:
            minutes, seconds = divmod(remaining_time, 60)
            time_str = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=time_str)
            remaining_time -= 1
            self.master.after(1000, self.countdown, remaining_time)  # Call countdown every second
        else:
            self.timer_label.config(text="Time's up!")
            self.start_button.config(state=tk.NORMAL)
