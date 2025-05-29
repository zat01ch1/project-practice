# Отчет: Разработка текстового редактора на Python

## Шаг 1: Импорт библиотек
```python
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror
```
## Шаг 1: Инициализация переменных
```python
filename = None  
```
## Шаг 3: Функция создания нового файла
```python
def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)  
```
## Шаг 4: Функция сохранения файла
```python
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
```
## Шаг 5: Функция "Сохранить как"
```python
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
```
## Шаг 6: Функция открытия файла
```python
def openFile():
    global filename
    f = filedialog.askopenfile(mode='r')
    if f:
        t = f.read()
        text.delete(0.0, END)
        text.insert(0.0, t)  
        filename = f.name   
        f.close()
```
## Шаг 7: Создание графического интерфейса
```python
root = Tk()
root.title("Текстовый редактор Python")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

# Текстовое поле
text = Text(root, width=400, height=400)
text.pack()

# Меню
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
root.mainloop()  # Запуск основного цикла
```
Итоговая функциональность
Файловые операции:
    Создание/открытие/сохранение файлов
Поддержка формата .txt
Интерфейс:
    Текстовое поле с прокруткой
    Меню File с основными операциями

Обработка ошибок:
    Уведомления при проблемах с сохранением
