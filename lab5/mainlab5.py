from tkinter import *
from tkinter import messagebox as mb
import functional


def window_1(event):
    def get_result(event):
        entry_result.delete(0, END)
        try:
            soe_matrix = [[] for _ in range(row_n)]
            for i in range(row_n):
                for j in range(column_n):
                    soe_matrix[i].append(float(matrix[i][j].get()))

            final_result = functional.single_gauss(soe_matrix)
            for i in range(row_n):
                entry_result.insert(END, 'X{} = '.format(i+1))
                entry_result.insert(END, round(final_result[i], 8))
                entry_result.insert(END, '\t')
        except ValueError:
            mb.showerror(title='Помилка', message='Будь-ласка, введіть усі необхідні значення')
        except ZeroDivisionError:
            mb.showerror(title='Помилка', message='Ділення на нуль, перевірте правильність вводу даних')

    def insert_soe(event):
        for i in range(row_n):
            for j in range(column_n):
                matrix[i][j].delete(0, END)
                matrix[i][j].insert(0, functional.matrix_a[i][j])

    window1 = Toplevel(root)
    window1.title('Вікно розрахунку')
    window1.resizable(width=False, height=False)

    column_n = len(functional.matrix_a[0])
    row_n = len(functional.matrix_a)
    matrix = [[] for _ in range(row_n)]
    for i in range(row_n):
        for j in range(column_n-1):
            if j < column_n - 2:
                label = Label(window1, text='X{} +'.format(j+1), font='mincho 10')
            else:
                label = Label(window1, text='X{} ='.format(j+1), font='mincho 10')
            label.grid(row=i, column=j*2+1)
        for j in range(column_n):

            entry_matrix = Entry(window1, font='mincho 10', width=5)
            entry_matrix.grid(row=i, column=j*2)

            matrix[i].append(entry_matrix)

    button1 = Button(window1, text='Вставити готову систему', font='mincho 14', width=30)
    button_result = Button(window1, text='Результат:', font='mincho 14', width=30)

    button1.grid(row=row_n + 1, column=0, columnspan=column_n*2, padx=5, pady=2)
    button_result.grid(row=row_n + 2, column=0, columnspan=column_n*2, padx=5, pady=2)

    entry_result = Entry(window1, font='mincho 10', width=50)
    entry_result.grid(row=row_n + 3, column=0, columnspan=column_n*2, padx=5, pady=2)

    button1.bind('<Button-1>', insert_soe)
    button_result.bind('<Button-1>', get_result)


root = Tk()
width = root.winfo_screenwidth() // 2 - 275
height = root.winfo_screenheight() // 2 - 150
root.title('Голове меню')
root.geometry('550x300+{}+{}'.format(width, height))
root.resizable(width=False, height=False)

label1 = Label(root, text='Лабораторна робота №5', font='mincho 14', width=20)
label2 = Label(root, text='Студентки групи ІО-04', font='mincho 14')
label3 = Label(root, text='Кондратенко Вероніка', font='mincho 14')
label4 = Label(root, text='Варіант №8', font='mincho 14')

button1 = Button(root, text='До розрахунку', font='mincho 14', width=20)

button1.bind('<Button-1>', window_1)

for label, row in [(label1, 0), (label2, 1), (label3, 2), (label4, 3)]:
    label.grid(row=row, column=0, columnspan=1, sticky='w')

for button, column in [(button1, 1)]:
    button.grid(row=column, column=1, padx=125, ipady=5)

root.mainloop()
