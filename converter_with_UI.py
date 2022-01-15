import os
from tkinter import *

root = Tk()
root.title('Advanced Calculator')


def converter_func():
    try:
        base = int(base_input.get())
        num = int(number_input.get())
        number = num
        converted_string = ''
        quotient = num
        my_list = []
        if base == 16:
            base_16_func()
            converted_string = base_16_res
        else:
            while quotient >= base:
                rem = num % base
                quotient //= base
                num = quotient
                my_list.append(str(rem))
            else:
                my_list.append(str(quotient))

            my_list.reverse()
            for i in my_list:
                converted_string += i

        val.set(number)
        result.set(converted_string)
    except ValueError:
        pass


def base_16_func():
    global base_16_res
    base = int(base_input.get())
    num = int(number_input.get())
    converted_string = ''
    quotient = num
    my_list = []
    if base == 16:
        while quotient >= 16:
            quotient = num // 16
            rem = num % 16
            num = quotient
            my_list.append(str(rem))
        else:
            my_list.append(str(quotient))
        my_list.reverse()

        for i in range(len(my_list)):
            if my_list[i] == '10':
                my_list[i] = my_list[i].replace('10', 'A')
            elif my_list[i] == '11':
                my_list[i] = my_list[i].replace('11', 'B')
            elif my_list[i] == '12':
                my_list[i] = my_list[i].replace('12', 'C')
            elif my_list[i] == '13':
                my_list[i] = my_list[i].replace('13', 'D')
            elif my_list[i] == '14':
                my_list[i] = my_list[i].replace('14', 'E')
            elif my_list[i] == '15':
                my_list[i] = my_list[i].replace('15', 'F')
            else:
                pass
        for x in my_list:
            converted_string += x
        base_16_res = converted_string


def clear_func():
    number_input.delete(0, END)
    base_input.delete(0, END)


def calc_func():
    root.destroy()
    os.system('python3 advanced_calculator.py')


val = StringVar()
result = StringVar()


base_label = Label(root, text='Enter the base: ', padx=10, pady=10)
base_label.grid(row=1, column=0, sticky=W)

base_input = Entry(root)
base_input.grid(row=1, column=1, sticky=(W, E))

number_label = Label(root, text='Enter an integer to be converted:', padx=10, pady=5)
number_label.grid(row=0, column=0, sticky=W)

number_input = Entry(root)
number_input.grid(row=0, column=1, sticky=(W, E))

clear_button = Button(root, text='Clear', padx=80, pady=5, bg='#000', fg='#fff', command=clear_func)
clear_button.grid(row=2, column=0, sticky=W)

convert_button = Button(root, text='Convert', padx=80, pady=5, bg='#000', fg='#fff', command=converter_func)
convert_button.grid(row=2, column=1, sticky=E)

Label(root, textvariable=val, padx=5).grid(row=3, column=0, sticky=W)

result_label = Label(root, textvariable=result, padx=10, pady=5)
result_label.grid(row=3, column=1, sticky=W)

calc_button = Button(root, text='Calculator', bg='green', fg='white', command=calc_func)
calc_button.grid(row=4, column=0, columnspan=4, sticky='EW')

root.mainloop()
