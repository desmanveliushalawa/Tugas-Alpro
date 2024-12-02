import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.frame = root
        self.frame.columnconfigure(0, weight=1)

        self.entry = tk.Entry(self.frame, font=("Tmr", 12), justify="right")
        self.entry.grid(row=0, column=0, columnspan=6, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for text, row, col in buttons:
            button = tk.Button(self.frame, text=text, font=("tmr", 14),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=3, pady=4)

        for i in range(5):
            self.frame.rowconfigure(i, weight=1)
        for j in range(4):
            self.frame.columnconfigure(j, weight=1)

    def on_button_click(self, button):
        if button == "C":
            self.entry.delete(0, tk.END)
        elif button == "=":
            try:
                result = eval(self.entry.get())  # Evaluate the expression
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, button)
