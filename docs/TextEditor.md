# Отчет: Разработка текстового редактора на Python

## Шаг 1: Импорт библиотек
```python
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror

## Шаг 1: Инициализация переменных

filename = None  # Для хранения пути к текущему файлу

## Шаг 3: Функция создания нового файла
def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)  # Очистка текстового поля
