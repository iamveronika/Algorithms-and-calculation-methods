import random
import functional
import time
import external_file
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox as mb


def time_counter(array_a):
    begin_time = time.perf_counter()
    functional.heapsort(array_a)
    end_time = time.perf_counter()

    counted_time = end_time - begin_time
    return counted_time


def window_1(event):
    def get_result(event):
        entry2.delete(0, END)
        try:
            array_user = entry1.get().split()
            for i in range(len(array_user)):
                array_user[i] = float(array_user[i])
            functional.heapsort(array_user)
            entry2.insert(0, array_user)
        except ValueError:
            mb.showerror(title='Помилка', message='Потрібно вводити ЧИСЛА через "пробіл"')

    def get_file(event):
        entry1.delete(0, END)
        array_from_file = external_file.array_from_file()
        entry1.insert(END, array_from_file)

    window1 = Toplevel(root)
    width = window1.winfo_screenwidth() // 2 - 250
    height = window1.winfo_screenheight() // 2 - 150
    window1.title('Вікно 1')
    window1.geometry('500x300+{}+{}'.format(width, height))
    window1.resizable(width=False, height=False)

    label1 = Label(window1, text='Вікно сортування власного масиву', font='mincho 14', width=50)
    label2 = Label(window1, text='Будь-ласка, введіть необхідні параметри:', font='mincho 14', width=50)
    label3 = Label(window1, text='Масив:', font='mincho 14')
    label4 = Label(window1, text='Результат:', font='mincho 14')

    button1 = Button(window1, text='Відсортувати', font='mincho 14', width=10)
    button2 = Button(window1, text='Дані з файлу', font='mincho 14', width=10)

    entry1 = Entry(window1, font='mincho 14', width=20)
    entry2 = Entry(window1, font='mincho 14', width=20)

    label1.grid(row=0, column=0, sticky='w'+'e', columnspan=5)
    label2.grid(row=1, column=0, sticky='w'+'e', columnspan=5)
    label3.grid(row=2, column=1, sticky='e', columnspan=1)
    label4.grid(row=3, column=1, sticky='e', columnspan=1)

    entry1.grid(row=2, column=2, sticky='w')
    entry2.grid(row=3, column=2, sticky='w')
    button1.grid(row=3, column=0, sticky='w', padx=5, pady=2)
    button2.grid(row=2, column=0, sticky='w', padx=5, pady=2)

    button1.bind('<Button-1>', get_result)
    button2.bind('<Button-1>', get_file)


def window_2(event):
    time_array = [[], []]
    array1 = random.sample(range(1000000), 1000)
    array2 = random.sample(range(1000000), 2000)
    array3 = random.sample(range(1000000), 4000)
    array4 = random.sample(range(1000000), 8000)
    array5 = random.sample(range(1000000), 16000)
    array6 = random.sample(range(1000000), 32000)
    array7 = random.sample(range(1000000), 64000)
    array8 = random.sample(range(1000000), 128000)
    array9 = random.sample(range(1000000), 256000)
    array10 = random.sample(range(1000000), 512000)
    for array in [array1, array2, array3, array4, array5, array6, array7, array8, array9, array10]:
        tmp_list = time_counter(array)
        time_array[0].append(tmp_list*(10**6))
        time_array[1].append(len(array))
    print(time_array[0])
    print(time_array[1])

    f_theoretical = lambda n: n*np.log(n)
    fig = plt.subplots()
    n = np.linspace(1000, 512000, 1000)
    plt.plot(n, f_theoretical(n), label='Теоретичне значення')
    plt.plot(time_array[1], time_array[0], label='Практичне значення')
    plt.legend()

    plt.show()


root = Tk()
width = root.winfo_screenwidth() // 2 - 275
height = root.winfo_screenheight() // 2 - 150
root.title('Головне меню')
root.geometry('550x300+{}+{}'.format(width, height))
root.resizable(width=False, height=False)

label1 = Label(root, text='Лабораторна робота №2', font='mincho 14', width=20)
label2 = Label(root, text='Студентка групи ІО-04', font='mincho 14')
label3 = Label(root, text='Кондратенко Вероніка', font='mincho 14')
label4 = Label(root, text='Варіант №8', font='mincho 14')

button1 = Button(root, text='Відсортувати масив', font='mincho 14', width=20)
button2 = Button(root, text='Час виконання', font='mincho 14', width=20)

button1.bind('<Button-1>', window_1)
button2.bind('<Button-1>', window_2)

for label, row in [(label1, 0), (label2, 1), (label3, 2), (label4, 3)]:
    label.grid(row=row, column=0, columnspan=1, sticky='w')

for button, column in [(button1, 1), (button2, 2)]:
    button.grid(row=column, column=1, padx=125, ipady=5)

root.mainloop()
