import functions
import external_file
from tkinter import *
from tkinter import messagebox as mb


def window_1(event):
    def get_result(event):
        entry3.delete(0, END)
        try:
            b = float(entry1.get())
            c = float(entry2.get())
            final_result = functions.linear_algorithm(b, c)
            entry3.insert(END, final_result)
        except ValueError:
            mb.showerror(title='Помилка', message='Ви маєте вводити додатні числа')
        except OverflowError:
            mb.showerror(title='Помилка', message='Ви вводите занадто великі числа')

    def get_file(event):
        entry1.delete(0, END)
        entry2.delete(0, END)
        tmp_list = external_file.linear()
        b = float(tmp_list[0])
        c = float(tmp_list[1])
        entry1.insert(END, b)
        entry2.insert(END, c)

    window1 = Toplevel(root)
    width = window1.winfo_screenwidth() // 2 - 250
    height = window1.winfo_screenheight() // 2 - 150
    window1.title('Лінійний')
    window1.geometry('500x300+{}+{}'.format(width, height))
    window1.resizable(width=False, height=False)

    label1 = Label(window1, text='Приклад реалізації лінійного алгориму', font='mincho 14', width=50)
    label2 = Label(window1, text='Будь-ласка, введіть необхідні параметри:', font='mincho 14', width=50)
    label3 = Label(window1, text='b =', font='mincho 14')
    label4 = Label(window1, text='c =', font='mincho 14')
    label5 = Label(window1, text='Результат:', font='mincho 14')

    entry1 = Entry(window1, font='mincho 14', width=10)
    entry2 = Entry(window1, font='mincho 14', width=10)
    entry3 = Entry(window1, font='mincho 14', width=25)

    button1 = Button(window1, text='Обчислити', font='mincho 14', width=10)
    button2 = Button(window1, text='Дані з файлу', font='mincho 14', width=10)

    label1.grid(row=0, column=0, sticky='w'+'e', columnspan=5)
    label2.grid(row=1, column=0, sticky='w'+'e', columnspan=5)
    label3.grid(row=2, column=0, sticky='e', columnspan=1)
    label4.grid(row=2, column=2, sticky='e', columnspan=1)
    label5.grid(row=3, column=1, sticky='e', columnspan=1)

    entry1.grid(row=2, column=1, sticky='w')
    entry2.grid(row=2, column=3, sticky='w')
    entry3.grid(row=3, column=2, sticky='w', columnspan=2)

    button1.grid(row=3, column=0, sticky='w', padx=5, pady=2)
    button2.grid(row=2, column=0, sticky='w', padx=5, pady=2)

    button1.bind('<Button-1>', get_result)
    button2.bind('<Button-1>', get_file)


def window_2(event):
    def get_result(event):
        try:
            entry4.delete(0, END)
            a = float(entry1.get())
            b = float(entry2.get())
            x = float(entry3.get())

            final_result = functions.branched_algorithm(a, b, x)
            entry4.insert(END, final_result)
        except ValueError:
            mb.showerror(title='Помилка', message='Ви маєте вводити числа')
        except OverflowError:
            mb.showerror(title='Помилка', message='Ви вводите занадто великі числа')

    def get_file(event):
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        tmp_list = external_file.branched()
        a = float(tmp_list[0])
        b = float(tmp_list[1])
        x = float(tmp_list[2])
        entry1.insert(END, a)
        entry2.insert(END, b)
        entry3.insert(END, x)

    window2 = Toplevel(root)
    width = window2.winfo_screenwidth() // 2 - 250
    height = window2.winfo_screenheight() // 2 - 150
    window2.title('Розгалужений')
    window2.geometry('500x300+{}+{}'.format(width, height))
    window2.resizable(width=False, height=False)

    label1 = Label(window2, text='Приклад реалізації розгалуженого алгориму', font='mincho 14', width=50)
    label2 = Label(window2, text='Будь-ласка, введіть необхідні параметри:', font='mincho 14', width=50)
    label3 = Label(window2, text='a =', font='mincho 14')
    label4 = Label(window2, text='b =', font='mincho 14')
    label5 = Label(window2, text='x =', font='mincho 14')
    label6 = Label(window2, text='Результат:', font='mincho 14')

    entry1 = Entry(window2, font='mincho 14', width=10)
    entry2 = Entry(window2, font='mincho 14', width=10)
    entry3 = Entry(window2, font='mincho 14', width=10)
    entry4 = Entry(window2, font='mincho 14', width=25)

    button1 = Button(window2, text='Обчислити', font='mincho 14', width=10)
    button2 = Button(window2, text='Дані з файлу', font='mincho 14', width=10)

    label1.grid(row=0, column=0, sticky='w'+'e', columnspan=5)
    label2.grid(row=1, column=0, sticky='w'+'e', columnspan=5)
    label3.grid(row=2, column=0, sticky='e', columnspan=1)
    label4.grid(row=2, column=2, sticky='e', columnspan=1)
    label5.grid(row=3, column=2, sticky='e', columnspan=1)
    label6.grid(row=4, column=1, sticky='e', columnspan=1)

    entry1.grid(row=2, column=1, sticky='w')
    entry2.grid(row=2, column=3, sticky='w')
    entry3.grid(row=3, column=3, sticky='w')
    entry4.grid(row=4, column=2, sticky='w', columnspan=2)

    button1.grid(row=4, column=0, sticky='w', padx=5, pady=2)
    button2.grid(row=2, column=0, sticky='w', padx=5, pady=2)

    button1.bind('<Button-1>', get_result)
    button2.bind('<Button-1>', get_file)


def window_3(event):
    def get_result(event):
        try:
            entry5.delete(0, END)
            j = float(entry1.get())
            i = float(entry2.get())
            n1 = float(entry3.get())
            n2 = float(entry4.get())

            final_result = functions.cyclic_algorithm(j, i, n1, n2)
            entry5.insert(END, final_result)
        except ValueError:
            mb.showerror(title='Помилка', message='Ви маєте вводити числа')
        except OverflowError:
            mb.showerror(title='Помилка', message='Ви вводите занадто великі числа')

    def get_file(event):
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        tmp_list = external_file.cyclic()
        j = float(tmp_list[0])
        i = float(tmp_list[1])
        n1 = float(tmp_list[2])
        n2 = float(tmp_list[3])
        entry1.insert(END, j)
        entry2.insert(END, i)
        entry3.insert(END, n1)
        entry4.insert(END, n2)

    window3 = Toplevel(root)
    width = window3.winfo_screenwidth() // 2 - 250
    height = window3.winfo_screenheight() // 2 - 150
    window3.title('Циклічний')
    window3.geometry('500x300+{}+{}'.format(width, height))
    window3.resizable(width=False, height=False)

    label1 = Label(window3, text='Приклад реалізації циклічного алгориму', font='mincho 14', width=50)
    label2 = Label(window3, text='Будь-ласка, введіть необхідні параметри:', font='mincho 14', width=50)
    label3 = Label(window3, text='j =', font='mincho 14')
    label4 = Label(window3, text='i =', font='mincho 14')
    label5 = Label(window3, text='n1 =', font='mincho 14')
    label6 = Label(window3, text='n2 =', font='mincho 14')
    label7 = Label(window3, text='Результат:', font='mincho 14')

    entry1 = Entry(window3, font='mincho 14', width=10)
    entry2 = Entry(window3, font='mincho 14', width=10)
    entry3 = Entry(window3, font='mincho 14', width=10)
    entry4 = Entry(window3, font='mincho 14', width=10)
    entry5 = Entry(window3, font='mincho 14', width=25)

    button1 = Button(window3, text='Обчислити', font='mincho 14', width=10)
    button2 = Button(window3, text='Дані з файлу', font='mincho 14', width=10)

    label1.grid(row=0, column=0, sticky='w'+'e', columnspan=5)
    label2.grid(row=1, column=0, sticky='w'+'e', columnspan=5)
    label3.grid(row=2, column=0, sticky='e', columnspan=1)
    label4.grid(row=2, column=2, sticky='e', columnspan=1)
    label5.grid(row=3, column=0, sticky='e', columnspan=1)
    label6.grid(row=3, column=2, sticky='e', columnspan=1)
    label7.grid(row=4, column=1, sticky='e', columnspan=1)

    entry1.grid(row=2, column=1, sticky='w')
    entry2.grid(row=2, column=3, sticky='w')
    entry3.grid(row=3, column=1, sticky='w')
    entry4.grid(row=3, column=3, sticky='w')
    entry5.grid(row=4, column=2, sticky='w', columnspan=2)

    button1.grid(row=4, column=0, sticky='w', padx=5, pady=2)
    button2.grid(row=2, column=0, sticky='w', padx=5, pady=2)

    button1.bind('<Button-1>', get_result)
    button2.bind('<Button-1>', get_file)


root = Tk()
width = root.winfo_screenwidth() // 2 - 250
height = root.winfo_screenheight() // 2 - 150
root.title('Головне меню')
root.geometry('500x300+{}+{}'.format(width, height))
root.resizable(width=False, height=False)

label1 = Label(root, text='Лабораторна робота №1', font='mincho 14', width=20)
label2 = Label(root, text='Студентки групи ІО-04', font='mincho 14')
label3 = Label(root, text='Кондратенко Вероніки', font='mincho 14')
label4 = Label(root, text='Варіант №8', font='mincho 14')
label5 = Label(root, text='Вибір алгоритмів:', font='mincho 14')

button1 = Button(root, text='Лінійний', font='mincho 14', width=15)
button2 = Button(root, text='Розгалужений', font='mincho 14', width=15)
button3 = Button(root, text='Циклічний', font='mincho 14', width=15)

button1.bind('<Button-1>', window_1)
button2.bind('<Button-1>', window_2)
button3.bind('<Button-1>', window_3)

for label, row in [(label1, 0), (label2, 1), (label3, 2), (label4, 3)]:
    label.grid(row=row, column=0, columnspan=1, sticky='w')

label5.grid(row=0, column=1, columnspan=1, padx=125, ipady=10)

for button, column in [(button1, 1), (button2, 2), (button3, 3)]:
    button.grid(row=column, column=1, padx=125, ipady=5)

root.mainloop()
