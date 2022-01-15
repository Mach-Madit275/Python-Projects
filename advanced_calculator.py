import os

from tkinter import *
import math
root = Tk()
root.title('Advanced calculator')
# root.iconbitmap('/home/gson/Tkinter_Projects/Python_icon-icons.com_68975.ico')
# root.geometry('400x450')
LARGE_FONT = ('Arial', 25, 'bold')

operator = ' '


def default_screen():
    screen.insert(0, '0')


def button_click(num):
    if screen.get() == '0':
        screen.delete(0, END)
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(num))


def add_func(op):
    if ' = ' in small_screen.get():
        small_screen.delete(0, END)
    else:
        pass
    try:
        global n
        global operator
        operator = op
        n = float(screen.get())
        cast_on_small_screen()
        screen.delete(0, END)
    except:
        error = 'Syntax Error'
        screen.delete(0, END)
        screen.insert(0, error)

def sub_func(op):
    if ' = ' in small_screen.get():
        small_screen.delete(0, END)
    else:
        pass
    try:
        global n
        global operator
        operator = op
        n = float(screen.get())
        cast_on_small_screen()
        screen.delete(0, END)
    except:
        error = 'Syntax Error'
        screen.delete(0, END)
        screen.insert(0, error)


def mul_func(op):
    if ' = ' in small_screen.get():
        small_screen.delete(0, END)
    else:
        pass
    try:
        global n
        global operator
        operator = op
        n = float(screen.get())
        cast_on_small_screen()
        screen.delete(0, END)
    except:
        error = 'Syntax Error'
        screen.delete(0, END)
        screen.insert(0, error)


def div_func(op):
    if ' = ' in small_screen.get():
        small_screen.delete(0, END)
    else:
        pass
    try:
        global n
        global operator
        operator = op
        n = float(screen.get())
        cast_on_small_screen()
        screen.delete(0, END)
    except:
        error = 'Syntax Error'
        screen.delete(0, END)
        screen.insert(0, error)

def clear_func():
    screen.delete(0, END)
    small_screen.delete(0, END)
    default_screen()


def results_func(*args):
    try:
        n2 = float(screen.get())
        op_choice = operator
        small_screen.insert(100, ' ')
        small_screen.insert(100, op_choice)
        small_screen.insert(100, ' ')
        small_screen.insert(100, n2)
        small_screen.insert(100, ' = ')
        screen.delete(0, END)
        results = 0.0
        if op_choice == '+':
            results = n + n2
        elif op_choice == '-':
            results = n - n2
        elif op_choice == '*':
            results = n * n2
        elif op_choice == '/':
            results = n / n2
        else:
            pass
        screen.insert(0, results)
    except:
        error = 'Math Error'
        screen.delete(0, END)
        screen.insert(0, error)


def cast_on_small_screen():
    val = float(screen.get())
    small_screen.insert(0, val)


def converter_func():
    root.destroy()
    os.system('python3 converter_with_UI.py')

def Tan():
    result2 = float(screen.get())
    final_result = math.tan(result2 * math.pi / 180)
    # print('{0:8.4f}'.format(final_result))
    small_screen.delete(0, END)
    r = 'tan ' + str(result2) +" ="
    small_screen.insert(0, r)
    screen.delete(0, END)
    screen.insert(0, str(final_result))

def Cos():
    result2 = float(screen.get())
    final_result = math.cos(result2 * math.pi / 180)
    # print('{0:8.4f}'.format(final_result))
    small_screen.delete(0, END)
    r = 'cos ' + str(result2)+ " ="
    small_screen.insert(0, r)
    screen.delete(0, END)
    screen.insert(0, str(final_result))

def Sin():
    result2 = float(screen.get())
    final_result = math.sin(result2 * math.pi / 180)
    # print('{0:8.4f}'.format(final_result))
    small_screen.delete(0, END)
    r = 'sin ' + str(result2)+ " ="
    small_screen.insert(0, r)
    screen.delete(0, END)
    screen.insert(0, str(final_result))

def Log():
    result2 = float(screen.get())
    final_result = math.log10(result2)
    # print('{0:8.4f}'.format(final_result))
    small_screen.delete(0, END)
    r = 'log ' + str(result2)+ " ="
    small_screen.insert(0, r)
    screen.delete(0, END)
    screen.insert(0, str(final_result))
def square():
    result2=float(screen.get())
    final_result=math.pow(result2, 2)
    small_screen.delete(0,END)
    r=str(result2) + '\u00b2' + " ="
    small_screen.insert(0,r)
    screen.delete(0,END)
    screen.insert(0,str(final_result))


def squareroot():
    result2=float(screen.get())
    final_result=math.sqrt(result2)
    small_screen.delete(0,END)
    r="\u221A" + str(result2) + " ="
    small_screen.insert(0,r)
    screen.delete(0,END)
    screen.insert(0,str(final_result))


def cuberoot():
    result2=float(screen.get())
    final_result=math.pow(result2,1/3)
    small_screen.delete(0,END)
    r='\u221b' + str(result2) + " ="
    small_screen.insert(0,r)
    screen.delete(0,END)
    screen.insert(0,str(final_result))

def power():
    result2=float(screen.get())
    final_result=math.pow(result2,2)
    small_screen.delete(0,END)
    r=str(result2) + "^" + str(result2) + " ="
    small_screen.insert(0,r)
    screen.delete(0,END)
    screen.insert(0,str(final_result))

def delete():
    my_string = screen.get()
    my_string = my_string[:len(my_string) - 1]
    screen.delete(0, END)
    screen.insert(0, my_string)




small_screen = Entry(root, width=30, borderwidth=5)
small_screen.grid(row=0, column=0, columnspan=4, sticky=(E, S), padx=10)

screen = Entry(root, width=45, borderwidth=5, font='bold')
screen.grid(row=1, column=0, columnspan=4, sticky=(N, W, E, S), padx=10, pady=10)
# screen.focus()

# Defining the buttons
button_Square = Button(root, text="x\u00b2", padx=10, pady=10, bg='#000', fg='#fff', command=square)
button_Squareroot = Button(root, text="\u221Ax", padx=10, pady=10, bg='#000', fg='#fff', command=squareroot)
button_Power = Button(root, text='^', padx=10, pady=10, bg='#000', fg='#fff', command=power)
button_Cuberoot = Button(root, text='\u221b', padx=10, pady=10, bg='#000', fg='#fff', command=cuberoot)
button_Tan = Button(root, text='Tan', padx=10, pady=10, bg='#000', fg='#fff', command=Tan)
button_Cos = Button(root, text='Cos', padx=10, pady=10, bg='#000', fg='#fff', command=Cos)
button_Sin = Button(root, text='Sin', padx=10, pady=10, bg='#000', fg='#fff', command=Sin)
button_Log = Button(root, text='Log', padx=10, pady=10, bg='#000', fg='#fff', command=Log)
button_1 = Button(root, text='1', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: button_click(0))

# Additional Buttons
button_point = Button(root, text='.', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: button_click('.'))
button_converter = Button(root, text='converter', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=converter_func)

button_delete = Button(root, text='DEL', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=delete)
button_equal = Button(root, text='  =  ', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=results_func)
button_delete.grid(row=8, column=0, sticky=(W, E))
button_equal.grid(row=8, column=1, sticky=(W, E))
button_converter.grid(row=8, column=2, columnspan=2, sticky=(W, E))

# Defining Arithmetic Operators
button_add = Button(root, text='+', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: add_func('+'))
button_sub = Button(root, text='-', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: sub_func('-'))
button_mul = Button(root, text='x', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: mul_func('*'))
button_div = Button(root, text='÷', padx=10, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=lambda: div_func('/'))


# Defining Clear Button
button_clear = Button(root, text='AC', padx=0, pady=10, bg='#000', fg='#fff', font=LARGE_FONT, command=clear_func)

# Shoving and positioning the buttons to the screen
button_Square.grid(row=2, column=0, sticky=(W, E))
button_Squareroot.grid(row=2, column=1, sticky=(W, E))
button_Power.grid(row=2, column=2, sticky=(W, E))
button_Cuberoot.grid(row=2, column=3, sticky=(W, E))
button_Tan.grid(row=3, column=0, sticky=(W, E))
button_Cos.grid(row=3, column=1, sticky=(W, E))
button_Sin.grid(row=3, column=2, sticky=(W, E))
button_Log.grid(row=3, column=3, sticky=(W, E))
button_7.grid(row=4, column=0, sticky=(W, E))
button_8.grid(row=4, column=1, sticky=(W, E))
button_9.grid(row=4, column=2, sticky=(W, E))
button_add.grid(row=4, column=3, sticky=(W, E))

button_4.grid(row=5, column=0, sticky=(W, E))
button_5.grid(row=5, column=1, sticky=(W, E))
button_6.grid(row=5, column=2, sticky=(W, E))
button_sub.grid(row=5, column=3, sticky=(W, E))

button_1.grid(row=6, column=0, sticky=(W, E))
button_2.grid(row=6, column=1, sticky=(W, E))
button_3.grid(row=6, column=2, sticky=(W, E))
button_mul.grid(row=6, column=3, sticky=(W, E))

button_0.grid(row=7, column=0, sticky=(W, E))
button_point.grid(row=7, column=1, sticky=(W, E))
button_clear.grid(row=7, column=2, sticky=(W, E))
button_div.grid(row=7, column=3, sticky=(W, E))

default_screen()
root.bind('<Return>', results_func)
root.mainloop()
