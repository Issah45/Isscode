from tkinter import *
from tkinter import filedialog
from tkcode import CodeEditor

root = Tk()

root.title("Isscode")
root.geometry("600x400")
root.iconbitmap("@icon.xbm")

# new file function
def new_file():
    root.title("New File - Isscode")
    code.delete("1.0", END)

#open file function
def open_file():
    code.delete("1.0", END)
    f = filedialog.askopenfilename(title="Open File")
    root.title(f"{f} - Isscode")

    f = open(f, "r").read()
    code.insert(END, f)
    
    f.close()

# save file function
def save_file():
    f = filedialog.asksaveasfilename(title="Save File")
    if f:
        root.title(f"{f} - Isscode")

    f = open(f, "w")
    f.write(code.get(1.0, END))
    f.close()

# main frame
main_frame = Frame(root)
main_frame.pack()

# text box
code = CodeEditor(main_frame, font="Consolas", language="python")
code.pack()

# menu
main_menu = Menu(root)
root.config(menu=main_menu)

# file menu
file_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit")

root.mainloop()
