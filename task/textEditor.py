from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    if filename:
        t = text.get(0.0, END)
        try:
            with open(filename, 'w') as f:
                f.write(t)
        except:
            showerror(title='Ой!', message="Не удается сохранить файл")
    else:
        saveAs()

def saveAs():
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if f:
        t = text.get(0.0, END)
        try:
            f.write(t.rstrip())
            f.close()
            global filename
            filename = f.name
        except:
            showerror(title='Ой!', message="Не удается сохранить файл")

def openFile():
    global filename
    f = filedialog.askopenfile(mode='r')
    if f:
        t = f.read()
        text.delete(0.0, END)
        text.insert(0.0, t)
        filename = f.name
        f.close()

root = Tk()
root.title("Текстовый редактор Python")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="SaveAs", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()