from tkinter import *


class Calculator:
    def __init__(self, window):
        self.expression = StringVar()
        self.create_gui(window)

    def create_gui(self, window):

        # Entry widget to display the calculation
        entry = Entry(window, textvariable=self.expression, font=('Arial', 24), state="readonly")
        entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create button widgets
        button_values = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+'
        ]

        for i, value in enumerate(button_values):
            row = i // 4 + 1
            column = i % 4
            button = Button(window, text=value, width=5, height=2, font=('Arial', 16, 'bold'),
                            command=lambda val=value: self.expression.set(self.expression.get() + val))
            button.grid(row=row, column=column, padx=5, pady=5)

        # Clear and equals button
        clear_button = Button(window, text='C', width=5, height=2, font=('Arial', 16, 'bold'),
                              command=lambda: self.expression.set(''))
        clear_button.grid(row=5, column=0, padx=10, pady=10)

        equal_button = Button(window, text='=', width=5, height=2, font=('Arial', 16, 'bold'),
                              command=lambda: self.calculate())
        equal_button.grid(row=5, column=3, padx=5, pady=5)

        window.configure(bg='#282828')

    def calculate(self):
        try:
            result = str(eval(self.expression.get()))
            self.expression.set(result)
        except:
            self.expression.set('Error')
