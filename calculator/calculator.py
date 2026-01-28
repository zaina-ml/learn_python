from tkinter import *

expression = ''

def press(num):
    global expression

    expression = expression + str(num)
    equation.set(expression)

def clear():
    global expression
    expression = ''
    equation.set(0)

def equal_press():
    global expression

    if not expression:
        return 0
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = str(total)
    except:
        equation.set('ERROR')
        expression = ''


window = Tk()
window.title("Calculator")

window.geometry('355x475')
window.configure(bg = '#5c85d6')
window.resizable(False, False)

img = PhotoImage(file = 'calc.png')
window.iconphoto(False, img)


button_frame = Frame(window, bg = '#5c85d6')

equation = StringVar()
equation.set('0')

calculator_screen = Entry(button_frame, textvariable = equation, justify = 'right', font = ('arial', 20, 'bold'), bg  = '#000033', fg = '#ffffff')
calculator_screen.pack()

button_frame.pack()

button_1 = Button(button_frame, text = 1, font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: press(1))
button_2 = Button(button_frame, text = 2, font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: press(2))
button_3 = Button(button_frame, text = 3, font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: press(3))
button_add = Button(button_frame, text = '+', font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: press('+'))

button_4 = Button(button_frame, text = 4, font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: press(4))
button_5 = Button(button_frame, text = 5, font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: press(5))
button_6 = Button(button_frame, text = 6, font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: press(6))
button_subtract = Button(button_frame, text = '-', font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: press('-'))

button_7 = Button(button_frame, text = 7, font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: press(7))
button_8 = Button(button_frame, text = 8, font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: press(8))
button_9 = Button(button_frame, text = 9, font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: press(9))
button_multiply = Button(button_frame, text = '*', font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: press('*'))

button_0 = Button(button_frame, text = 0, font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', command = lambda: press(0))
button_decimal = Button(button_frame, text = '.', font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: press('.'))

button_clear = Button(button_frame, text = 'C', font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = clear)
button_divide = Button(button_frame, text = '/', font = ('times new roman', 12), borderwidth = 1, width = 8, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: press('/'))

button_equal = Button(button_frame, text = '=', font = ('times new roman', 12), borderwidth = 1, width = 35, height = 3, bg = '#fff746', relief = 'ridge', command = lambda: equal_press())


calculator_screen.grid(row = 0, column = 0, columnspan = 4, ipadx = 8, ipady = 25, pady = 15)

button_1.grid(row = 1, column = 0, sticky = 'nsew')
button_2.grid(row = 1, column = 1, sticky = 'nsew')
button_3.grid(row = 1, column = 2, sticky = 'nsew')
button_add.grid(row = 1, column = 3, sticky = 'nsew')

button_4.grid(row = 2, column = 0, sticky = 'nsew')
button_5.grid(row = 2, column = 1, sticky = 'nsew')
button_6.grid(row = 2, column = 2, sticky = 'nsew')
button_subtract.grid(row = 2, column = 3, sticky = 'nsew')

button_7.grid(row = 3, column = 0, sticky = 'nsew')
button_8.grid(row = 3, column = 1, sticky = 'nsew')
button_9.grid(row = 3, column = 2, sticky = 'nsew')
button_multiply.grid(row = 3, column = 3, sticky = 'nsew')

button_0.grid(row = 4, column  = 0, sticky = 'nsew')
button_decimal.grid(row = 4, column = 1, sticky = 'nsew')
button_clear.grid(row = 4, column = 2, sticky = 'nsew')
button_divide.grid(row = 4, column = 3, sticky = 'nsew')

button_equal.grid(row = 5, column = 0, sticky = 'nsew', columnspan = 4)

window.mainloop()