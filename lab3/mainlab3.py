from tkinter import *
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
import numpy as np

np.seterr(divide='ignore', invalid='ignore')

class Table(Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings

        for head in headings:
            table.heading(head, text=head, anchor=CENTER)
            table.column(head, anchor=CENTER)

        for row in rows:
            table.insert('', END, values=tuple(row))

        scrolltable = Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=RIGHT, fill=Y)
        table.pack(expand=YES, fill=BOTH)


def window_1(event):
    def f(x):
        return np.sin(x)

    def lagranz(node, function):
        n = node.size

        def polynomial(x):
            z = 0
            for j in range(n):
                def action(j, n):
                    result = 1
                    for i in range(n):
                        if i == j:
                            continue
                        result *= (x - node[i]) / (node[j] - node[i])
                    return result
                z += action(j, n) * function[j]
            return z
        return polynomial

    def chart(event):
        fig = plt.subplots(1)
        plt.subplot(211)
        plt.plot(x_new, f(x_new), label='Оригінальна функція sin(x)')
        plt.plot(x_new, lag_pol(x_new), label='Поліном Лагранжа')
        plt.legend()
        plt.subplot(212)
        plt.plot(x_new, f(x_new) - lag_pol(x_new), label='Похибка')
        plt.legend()

        plt.show()

    def table(event):
        for_table = [(round(x_new[i], 3), delta_n[i], delta_exact[i], k[i]) for i in range(len(k))]
        window_table = Toplevel(window1)
        window_table.title('Таблиця для sin(x)')
        table = Table(window_table, headings=('x', 'Δn', 'Δexact', 'k'), rows=for_table)
        table.pack(expand=YES, fill=BOTH)

    a = 0
    b = 2
    h = (b - a) / 10
    x = np.arange(a, b + 0.1, h)
    y = f(x)
    lag_pol = lagranz(x, y)
    x_new = np.arange(a, b + 0.01, 0.1)

    x_n = np.arange(a, b + 0.1, (b - a) / 12)
    y_n = f(x_n)
    lag_pol_n = lagranz(x_n, y_n)

    delta_n = lag_pol(x_new) - lag_pol_n(x_new)
    delta_exact = lag_pol(x_new) - f(x_new)
    k = 1 - delta_exact / delta_n

    delta_n = delta_n.tolist()
    delta_exact = delta_exact.tolist()
    k = k.tolist()
    x_new = x_new.tolist()

    window1 = Toplevel(root)
    window1.title('sin(x)')
    window1.resizable(width=False, height=False)

    button1 = Button(window1, text='Графік для sin(x)', font='mincho 14', width=30)
    button2 = Button(window1, text='Таблиця для sin(x)', font='mincho 14', width=30)

    button1.grid(row=3, column=0, sticky='w', padx=5, pady=2)
    button2.grid(row=2, column=0, sticky='w', padx=5, pady=2)

    button1.bind('<Button-1>', chart)
    button2.bind('<Button-1>', table)


def window_2(event):
    def f(x):
        return np.cos(x + (np.cos(x) ** 3))

    def lagranz(node, function):
        n = node.size

        def polynomial(x):
            z = 0
            for j in range(n):
                def action(j, n):
                    result = 1
                    for i in range(n):
                        if i == j:
                            continue
                        result *= (x - node[i]) / (node[j] - node[i])
                    return result
                z += action(j, n) * function[j]
            return z
        return polynomial

    def chart(event):
        fig = plt.subplots(2)
        plt.subplot(211)
        plt.plot(x_new, f(x_new), label='Оригінальна функція cos(x+cos^3(x))')
        plt.plot(x_new, lag_pol(x_new), label='Поліном Лагранжа')
        plt.legend()
        plt.subplot(212)
        plt.plot(x_new, f(x_new) - lag_pol(x_new), label='Похибка')
        plt.legend()

        plt.show()

    def table(event):
        for_table = [(round(x_new[i], 3), delta_n[i], delta_exact[i], k[i]) for i in range(len(k))]
        window_table = Toplevel(window2)
        window_table.title('Таблиця для cos(x+cos^3(x))')
        table = Table(window_table, headings=('x', 'Δn', 'Δexact', 'k'), rows=for_table)
        table.pack(expand=YES, fill=BOTH)

    a = 0
    b = 2
    h = (b - a) / 10
    x = np.arange(a, b + 0.1, h)
    y = f(x)
    lag_pol = lagranz(x, y)
    x_new = np.arange(a, b + 0.01, 0.1)

    x_n = np.arange(a, b + 0.1, (b - a) / 12)
    y_n = f(x_n)
    lag_pol_n = lagranz(x_n, y_n)

    delta_n = lag_pol(x_new) - lag_pol_n(x_new)
    delta_exact = lag_pol(x_new) - f(x_new)
    k = 1 - delta_exact / delta_n

    delta_n = delta_n.tolist()
    delta_exact = delta_exact.tolist()
    k = k.tolist()
    x_new = x_new.tolist()

    window2 = Toplevel(root)
    window2.title('cos(x + cos^3(x))')
    window2.resizable(width=False, height=False)

    button1 = Button(window2, text='Графік для cos(x+cos^3(x))', font='mincho 14', width=30)
    button2 = Button(window2, text='Таблиця для cos(x+cos^3(x))', font='mincho 14', width=30)

    button1.grid(row=3, column=0, sticky='w', padx=5, pady=2)
    button2.grid(row=2, column=0, sticky='w', padx=5, pady=2)

    button1.bind('<Button-1>', chart)
    button2.bind('<Button-1>', table)


root = Tk()
width = root.winfo_screenwidth() // 2 - 275
height = root.winfo_screenheight() // 2 - 150
root.title('Головне меню')
root.geometry('550x300+{}+{}'.format(width, height))
root.resizable(width=False, height=False)

label1 = Label(root, text='Лабораторна робота №3', font='mincho 14', width=20)
label2 = Label(root, text='Студентки групи ІО-04', font='mincho 14')
label3 = Label(root, text='Кондратенко Вероніка', font='mincho 14')
label4 = Label(root, text='Варіант №8', font='mincho 14')

button1 = Button(root, text='sin(x)', font='mincho 14', width=20)
button2 = Button(root, text='cos(x + cos^3(x))', font='mincho 14', width=20)

button1.bind('<Button-1>', window_1)
button2.bind('<Button-1>', window_2)

for label, row in [(label1, 0), (label2, 1), (label3, 2), (label4, 3)]:
    label.grid(row=row, column=0, columnspan=1, sticky='w')

for button, column in [(button1, 1), (button2, 2)]:
    button.grid(row=column, column=1, padx=125, ipady=5)

root.mainloop()
