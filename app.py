from tkinter import Tk, Canvas, Label, Entry, Button

class MyWindow:

def __init__(self):

self.window = Tk()

self.window.geometry("700x700")

self.window.title("АВТОСЕРВИС Cat & Co")

self.window.config(bg='blue')

self.window.resizable(width=False, height=False)

self._my_canvas() # Создание холста

self._new_labels() # Создание надписей

self._new_entries() # Создание полей ввода

self._new_button() # Создание кнопок

self.window.mainloop()

def _my_canvas(self):

"""Создание и размещение холста."""

self.canvas = Canvas(self.window, width=670, height=670, bg='lightblue')

self.canvas.pack(expand=True) # expand=True заполняет всё доступное пространство

def _new_labels(self):

"""Создание и размещение текстовых надписей."""

MyLabel(master=self.canvas, text="Автосервис CAT & Co", font=("Arial", 20), color="lightblue", x=180, y=50)

MyLabel(master=self.canvas, text="Марка автомобиля:", font=("Arial", 15), color="lightblue", x=50, y=100)

MyLabel(master=self.canvas, text="Модель автомобиля:", font=("Arial", 15), color="lightblue", x=50, y=150)

MyLabel(master=self.canvas, text="Цвет автомобиля:", font=("Arial", 15), color="lightblue", x=50, y=200)

MyLabel(master=self.canvas, text="Год производства:", font=("Arial", 15), color="lightblue", x=50, y=250)

MyLabel(master=self.canvas, text="Номер автомобиля:", font=("Arial", 15), color="lightblue", x=50, y=300)

def _new_entries(self):

"""Создание и размещение полей ввода."""

MyEntry(master=self.canvas, font=("Arial", 15), x=270, y=100, width=150) # Марка

MyEntry(master=self.canvas, font=("Arial", 15), x=270, y=150, width=150) # Модель

MyEntry(master=self.canvas, font=("Arial", 15), x=270, y=200, width=150) # Цвет

MyEntry(master=self.canvas, font=("Arial", 15), x=270, y=250, width=150) # Год

MyEntry(master=self.canvas, font=("Arial", 15), x=270, y=300, width=150) # Номер

def _new_button(self):

"""Создание и размещение кнопок."""

MyButton(master=self.canvas, text="Записать", font=("Arial", 15), x=500, y=600, width=100)

class MyLabel:

"""Класс для создания текстовых надписей (меток)."""

def __init__(self, master, text, font, color, x, y):

self.text = text

self.x = x

self.y = y

self.font = font

self.color = color

self.master = master # Канва, на которой размещается надпись

self.label = Label(master=master, text=self.text, font=self.font, bg=self.color)

self.label.place(x=self.x, y=self.y)

class MyEntry:

"""Класс для создания полей ввода."""

def __init__(self, master, font, x, y, width):

self.master = master

self.font = font

self.x = x

self.y = y

self.width = width

self.entry = Entry(master=master, font=self.font, width=width)

self.entry.place(x=self.x, y=self.y)

class MyButton:

"""Класс для создания кнопок."""

def __init__(self, master, text, font, x, y, width):

self.text = text # текст на кнопке

self.x = x # координата по х

self.y = y # координата по у

self.font = font # размер шрифта

self.width = width # ширина кнопки

self.master = master

self.button = Button(master=master, text=self.text, font=self.font)

self.button.place(x=self.x, y=self.y, width=self.width)

if __name__ == "__main__":

window = MyWindow()