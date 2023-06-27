from tkinter import *
from tkinter import messagebox as mb
import functional
import matplotlib.pyplot as plt
import numpy as np

np.seterr(divide='ignore', invalid='ignore')

def window_1(event):
    def get_result(event):
        entry4.delete(0, END)
        try:
            a = float(entry1.get())
            b = float(entry2.get())
            e = float(entry3.get())
            final_result = functional.newton(a, b, e)
            entry4.insert(END, round(abs(final_result[0]), 16))
            entry4.insert(END, ' Кіл. ітерацій = ')
            entry4.insert(END, final_result[1])

        except ValueError:
            mb.showerror(title='Помилка', message='Будь-ласка, введіть межі')
        except TypeError:
            mb.showerror(title='Помилка', message='Будь-ласка, введіть інші межі')
        except ZeroDivisionError:
            mb.showerror(title='Помилка', message='Будь-ласка, введіть інші межі')


    window1 = Toplevel(root)
    window1.title('Вікно розрахунку')
    window1.resizable(width=False, height=False)

    label1 = Label(window1, text='Ліва межа:', font='mincho 10')
    label2 = Label(window1, text='Права межа:', font='mincho 10')
    label3 = Label(window1, text='Точність ε:', font='mincho 10')

    entry1 = Entry(window1, font='mincho 10', width=10)
    entry2 = Entry(window1, font='mincho 10', width=10)
    entry3 = Entry(window1, font='mincho 10', width=10)
    entry4 = Entry(window1, font='mincho 14', width=35)

    button1 = Button(window1, text='Результат:', font='mincho 14', width=30)

    for label, column in [(label1, 0), (label2, 1), (label3, 2)]:
        label.grid(row=1, column=column, columnspan=1, sticky='w')

    for entry, column in [(entry1, 0), (entry2, 1), (entry3, 2)]:
        entry.grid(row=2, column=column, columnspan=1, sticky='w')

    entry4.grid(row=4, column=0, columnspan=3, sticky='w')

    button1.grid(row=3, column=0, columnspan=3, sticky='w', padx=5, pady=2)

    button1.bind('<Button-1>', get_result)


def window_2(event):
    def f(x):
        return (np.sin(x + np.pi / 2)) ** 2 - (x ** 2) / 4

    x = np.linspace(0, 6, 100)

    fig = plt.subplots(1)
    plt.subplot(111)
    plt.plot(x, f(x), label='Функція (sin(x+π/2))^2 - (x^2)/4')
    plt.legend()

    plt.show()


root = Tk()
width = root.winfo_screenwidth() // 2 - 275
height = root.winfo_screenheight() // 2 - 150
root.title('Головне меню')
root.geometry('550x300+{}+{}'.format(width, height))
root.resizable(width=False, height=False)

label1 = Label(root, text='Лабораторна робота №4', font='mincho 14', width=20)
label2 = Label(root, text='Студентка групи ІО-04', font='mincho 14')
label3 = Label(root, text='Кондратенко Вероніка', font='mincho 14')
label4 = Label(root, text='Варіант №8', font='mincho 14')

button1 = Button(root, text='(sin(x+π/2))^2 - (x^2)/4', font='mincho 14', width=20)
button2 = Button(root, text='Графік функції', font='mincho 14', width=20)

button1.bind('<Button-1>', window_1)
button2.bind('<Button-1>', window_2)


for label, row in [(label1, 0), (label2, 1), (label3, 2), (label4, 3)]:
    label.grid(row=row, column=0, columnspan=1, sticky='w')

for button, column in [(button1, 1), (button2, 2)]:
    button.grid(row=column, column=1, padx=125, ipady=5)

root.mainloop()
