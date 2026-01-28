from tkinter import *
from ttkbootstrap import Style

currentX = 0
currentY = 0
drawWidth = 5
color = 'black'


def locate_coords(event):
    global currentX, currentY
    currentX, currentY = event.x, event.y


def add_line(event):
    global drawWidth
    global currentX, currentY
    canvas.create_line((currentX, currentY, event.x, event.y), fill=color, width=drawWidth)
    currentX, currentY = event.x, event.y


def changeColor(newColor):
    global color
    color = newColor


def clearCanvas():
    canvas.delete('all')
    display_pallet()


style = Style()
style = Style(theme='flatly')

fontStyle = ("Calibri", 16)

window = style.master
window.state('zoomed')

window.title("Paint")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

canvas = Canvas(window)
canvas.grid(row=0, column=0, sticky='nsew')

menubar = Menu(window)
window.config(menu=menubar)
submenu = Menu(menubar)
menubar.add_cascade(label='File', menu=submenu)

submenu.add_command(label='New Canvas', command=clearCanvas)

canvas.bind('<Button-1>', locate_coords)
canvas.bind('<B1-Motion>', add_line)


def display_pallet():
    id = canvas.create_rectangle((10, 10, 30, 30), fill="yellow")
    canvas.tag_bind(id, '<Button-1>', lambda x: changeColor("yellow"))

    id = canvas.create_rectangle((10, 40, 30, 60), fill="red")
    canvas.tag_bind(id, '<Button-1>', lambda x: changeColor("red"))

    id = canvas.create_rectangle((10, 70, 30, 90), fill="blue")
    canvas.tag_bind(id, '<Button-1>', lambda x: changeColor("blue"))

    id = canvas.create_rectangle((10, 100, 30, 120), fill="green")
    canvas.tag_bind(id, '<Button-1>', lambda x: changeColor("green"))

    id = canvas.create_rectangle((10, 130, 30, 150), fill="orange")
    canvas.tag_bind(id, '<Button-1>', lambda x: changeColor("orange"))

    id = canvas.create_rectangle((10, 160, 30, 180), fill="pink")
    canvas.tag_bind(id, '<Button-1>', lambda x: changeColor("pink"))

    id = canvas.create_rectangle((10, 190, 30, 210), fill="black")
    canvas.tag_bind(id, '<Button-1>', lambda x: changeColor("black"))


display_pallet()

window.mainloop()
