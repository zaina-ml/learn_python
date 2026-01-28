import os

from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
from tkinter import colorchooser

from ttkbootstrap import Style

style = Style()

window = style.master

window.geometry("1216x644")
window.wait_visibility(window)
window.title("New File - Text Editor")

global open_status_name
global selected
selected = False
open_status_name = False
text_file = ''


# File Menu

def new_file():
    editor.delete(1.0, END)
    window.title("New File - Text Editor")
    status.config(text="New File")


def open_file():
    global text_file


    editor.delete(1.0, END)

    text_file = filedialog.askopenfilename(initialdir="C:/Desktop", title="Open File", filetypes=(
        ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All Files", "*.* "), ("Python Files", "*.py")))

    if text_file:
        global open_status_name
        open_status_name = text_file

    name = text_file
    name2 = os.path.basename(text_file)

    status.config(text=name)
    window.title(name2 + " - " + "Text Editor")

    tf = open(text_file, 'r')
    openFile = tf.read()

    editor.insert(END, openFile)

    tf.close()


def save_as_file():
    global text_file
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Desktop", title="Save File",
                                             filetypes=(
                                                 ("Text Files", "*.txt"), ("HTML Files", "*.html"),
                                                 ("All Files", "*.* "),
                                                 ("Python Files", "*.py")))

    name = text_file
    name2 = os.path.basename(text_file)

    status.config(text=name)
    window.title(name2 + " - " + "Text Editor")


    name = text_file
    name2 = os.path.basename(text_file)

    status.config(text=name)
    window.title(name2 + " - " + "Text Editor")



def save_file():
    global open_status_name, text_file


    tf = open(text_file, 'w')
    tf.write(editor.get(1.0, END))
    tf.close()


    messagebox.showinfo("Alert", "File Saved")



def quitEditor():
    window.destroy()

# Edit Menu

def cut_text(e):
    global selected
    if selected:
        selected = editor.selection_get()

        editor.delete("sel.first", "sel.last")
    else:
        messagebox.showerror("Error", "Please Select An Area To Cut")


def copy_text(e):
    global selected
    if selected:
        selected = editor.selection_get()


def paste_text(e):
    if selected:
        pos = editor.index(INSERT)
        editor.insert(pos, selected)


def bold_text():
    bold_font = font.Font(editor, editor.cget('font'))
    bold_font.configure(weight="bold")

    editor.tag_configure("bold", font = bold_font)
    try:
        current_tags = editor.tag_names("sel.first")

        if "bold" in current_tags:
            editor.tag_remove("bold", "sel.first", "sel.last")
        else:
            editor.tag_add("bold", "sel.first", "sel.last" )
    except:
        messagebox.showerror("Error", "Please Select An Area To Bolden")



def italic_text():
    italic_font = font.Font(editor, editor.cget('font'))
    italic_font.configure(slant="italic")

    editor.tag_configure("italic", font = italic_font)

    try:
        current_tags = editor.tag_names("sel.first")

        if "italic" in current_tags:
            editor.tag_remove("italic", "sel.first", "sel.last")
        else:
            editor.tag_add("italic", "sel.first", "sel.last" )
    except:
        messagebox.showerror("Error", "Please Select An Area To Italicize")


def color_text():
    text_color = colorchooser.askcolor()[1]
    if text_color:
        color_font = font.Font(editor, editor.cget('font'))


        editor.tag_configure("color", font = color_font, foreground=text_color)

        try:
            current_tags = editor.tag_names("sel.first")

            if "color" in current_tags:
                editor.tag_remove("color", "sel.first", "sel.last")
            else:
                editor.tag_add("color", "sel.first", "sel.last" )
        except:
            messagebox.showerror("Error", "Please Select An Area To Change The Font Color")


storeText = Frame(window)

storeText.pack()


textscroll = Scrollbar(storeText)
textscroll.pack(side=RIGHT, fill=Y, padx=5, pady=5)

editor = Text(storeText, bg="white", width=97, height=25, font=("Helvetica", 16), selectbackground="lightblue",
              insertbackground="black",
              selectforeground="black", undo=True, fg="black", yscrollcommand=textscroll.set)

editor.configure(font=("Consolas", 16))


menubar = Menu(window)
window.config(menu=menubar)
file = Menu(menubar, tearoff=False)
menubar.add_cascade(label='File', menu=file)

file.add_command(label='New', command=new_file)
file.add_command(label='Open', command=open_file)
file.add_command(label='Save', command=save_file)
file.add_command(label='Save As', command=save_as_file)
file.add_separator()
file.add_command(label='Exit', command=quitEditor)

edit = Menu(menubar, tearoff=False)
menubar.add_cascade(label='Edit', menu=edit)

edit.add_command(label='Cut', command=lambda: cut_text(False), accelerator="(Ctrl + X)")
edit.add_command(label='Copy', command=lambda: copy_text(False), accelerator="(Ctrl + C)")
edit.add_command(label='Paste', command=lambda: paste_text(False), accelerator="(Ctrl + V)")
edit.add_separator()
edit.add_command(label='Undo',  accelerator="(Ctrl + Z)", command=editor.edit_undo)
edit.add_command(label='Redo',  accelerator="(Ctrl + S)", command=editor.edit_redo)

preference = Menu(menubar, tearoff=False)


format = Menu(menubar, tearoff=False)
menubar.add_cascade(label='Formatting', menu = format)

format.add_command(label='Font Color', command=color_text)
format.add_separator()
format.add_command(label='Bolden Text', command=bold_text)
format.add_command(label='Italicize Text', command=italic_text)


editor.pack(padx=2, pady=2)

textscroll.config(command=editor.yview)

status = Label(window, text='Untitled', anchor=E)
status.pack(fill=X, side=BOTTOM, ipady=5, padx=2, pady=2)


window.bind('<Control-Key-x>', cut_text)
window.bind('<Control-Key-c>', copy_text)
window.bind('<Control-Key-v>', paste_text)


window.mainloop()
