import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("Hesap Makinesi - Utku")
        # setting window size
        width = 450
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.result_var = tk.StringVar()
        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()

        # Labels
        GLabel_454 = tk.Label(root, text="RAKAM1")
        ft = tkFont.Font(family='Times', size=10)
        GLabel_454["font"] = ft
        GLabel_454.place(x=110, y=90, width=70, height=25)

        GLabel_999 = tk.Label(root, text="RAKAM2")
        GLabel_999["font"] = ft
        GLabel_999.place(x=180, y=90, width=70, height=25)

        GLabel_382 = tk.Label(root, text="SONUC")
        GLabel_382["font"] = ft
        GLabel_382.place(x=250, y=90, width=70, height=25)

        # Entry fields
        self.entry1 = tk.Entry(root, textvariable=self.num1_var)
        self.entry1.place(x=110, y=160, width=70, height=25)

        self.entry2 = tk.Entry(root, textvariable=self.num2_var)
        self.entry2.place(x=190, y=160, width=70, height=25)

        self.result_entry = tk.Entry(root, textvariable=self.result_var, state='readonly')
        self.result_entry.place(x=270, y=160, width=70, height=25)

        # Operator buttons
        operators = {'+': self.addition, '-': self.subtraction, 'x': self.multiplication}
        x_pos = 110
        for op, command in operators.items():
            btn = tk.Button(root, text=op, command=command)
            btn.place(x=x_pos, y=250, width=50, height=25)
            x_pos += 60

        # Percentage button
        btn_percentage = tk.Button(root, text="%", command=self.percentage)
        btn_percentage.place(x=110, y=420, width=50, height=25)

        # Number buttons
        for i in range(1, 10):
            btn = tk.Button(root, text=str(i), command=lambda n=i: self.append_number(n))
            x_pos = 110 + ((i - 1) % 3) * 60
            y_pos = 300 + ((i - 1) // 3) * 40
            btn.place(x=x_pos, y=y_pos, width=50, height=25)

        # Zero button (to the right of percentage)
        btn_zero = tk.Button(root, text="0", command=lambda: self.append_number(0))
        btn_zero.place(x=170, y=420, width=50, height=25)

        # Division button (to the right of 0)
        btn_division = tk.Button(root, text="/", command=self.division)
        btn_division.place(x=230, y=420, width=50, height=25)

    def append_number(self, number):
        if self.entry1.focus_get() == self.entry1:
            self.num1_var.set(self.num1_var.get() + str(number))
        elif self.entry2.focus_get() == self.entry2:
            self.num2_var.set(self.num2_var.get() + str(number))

    def addition(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            self.result_var.set(num1 + num2)
        except ValueError:
            self.result_var.set("HATA")

    def subtraction(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            self.result_var.set(num1 - num2)
        except ValueError:
            self.result_var.set("HATA")

    def multiplication(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            self.result_var.set(num1 * num2)
        except ValueError:
            self.result_var.set("HATA")

    def division(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            if num2 != 0:
                self.result_var.set(num1 / num2)
            else:
                self.result_var.set("BÖLÜM YOK")
        except ValueError:
            self.result_var.set("HATA")

    def percentage(self):
        try:
            num1 = float(self.num1_var.get())
            self.result_var.set(num1 / 100)
        except ValueError:
            self.result_var.set("HATA")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
