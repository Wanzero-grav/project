from tkinter import Tk, Canvas, Label, Entry, Button

class MyWindow:

    def __init__(self):

        self.window = Tk()

        self.window.geometry("700x700")

        self.window.title("АВТОСЕРВИС Cat & Co")

        self.window.config(bg='blue')

        self.window.resizable(width=False, height=False)

        self._my_canvas()  # Создание холста

        self._new_labels()  # Создание надписей

        self._new_entries()  # Создание полей ввода

        self._new_button()  # Создание кнопок

        self.window.mainloop()

    def _my_canvas(self):

        self.canvas = Canvas(self.window, width=670, height=670, bg='lightblue', highlightthickness=0)  # highlightthickness=0 убирает рамку
        self.canvas.pack(expand=True)  # expand=True заполняет всё доступное пространство

    def _new_labels(self):

        MyLabel(master=self.canvas, text="Автосервис CAT & Co", font=("Arial", 20), color="black", bg_color="lightblue", x=180, y=50)
        MyLabel(master=self.canvas, text="Марка автомобиля:", font=("Arial", 15), color="black", bg_color="lightblue", x=50, y=100)
        MyLabel(master=self.canvas, text="Модель автомобиля:", font=("Arial", 15), color="black", bg_color="lightblue", x=50, y=150)
        MyLabel(master=self.canvas, text="Цвет автомобиля:", font=("Arial", 15), color="black", bg_color="lightblue", x=50, y=200)
        MyLabel(master=self.canvas, text="Год производства:", font=("Arial", 15), color="black", bg_color="lightblue", x=50, y=250)
        MyLabel(master=self.canvas, text="Номер автомобиля:", font=("Arial", 15), color="black", bg_color="lightblue", x=50, y=300)

    def _new_entries(self):

        self.brand_entry = MyEntry(master=self.canvas, font=("Arial", 15), x=270, y=100, width=150)  # Марка
        self.model_entry = MyEntry(master=self.canvas, font=("Arial", 15), x=270, y=150, width=150)  # Модель
        self.color_entry = MyEntry(master=self.canvas, font=("Arial", 15), x=270, y=200, width=150)  # Цвет
        self.year_entry = MyEntry(master=self.canvas, font=("Arial", 15), x=270, y=250, width=150)  # Год
        self.number_entry = MyEntry(master=self.canvas, font=("Arial", 15), x=270, y=300, width=150)  # Номер

    def _new_button(self):

        MyButton(master=self.canvas, text="Записать", font=("Arial", 15), x=500, y=600, width=100, command=self._save_data)

    def _save_data(self):
        """Функция для сохранения данных из полей ввода (пока просто выводит в консоль)."""
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        color = self.color_entry.get()
        year = self.year_entry.get()
        number = self.number_entry.get()

        print("Марка:", brand)
        print("Модель:", model)
        print("Цвет:", color)
        print("Год:", year)
        print("Номер:", number)

        # Здесь можно добавить код для записи данных в файл, базу данных и т.д.
        # Например:
        # with open("data.txt", "a") as f:
        #     f.write(f"{brand},{model},{color},{year},{number}\n")

class MyLabel:

    def __init__(self, master, text, font, color, bg_color, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.bg_color = bg_color
        self.master = master  # Канва, на которой размещается надпись
        self.label = Label(master=master, text=self.text, font=self.font, bg=self.bg_color, fg=self.color)  # fg - цвет текста
        self.label.place(x=self.x, y=self.y)


class MyEntry:

    def __init__(self, master, font, x, y, width):
        self.master = master
        self.font = font
        self.x = x
        self.y = y
        self.width = width
        self.entry = Entry(master=master, font=self.font, width=width)
        self.entry.place(x=self.x, y=self.y)

    def get(self):  # Метод для получения текста из Entry
        return self.entry.get()

class MyButton:

    def __init__(self, master, text, font, x, y, width, command=None):  # Добавлен параметр command
        self.text = text  # текст на кнопке
        self.x = x  # координата по х
        self.y = y  # координата по у
        self.font = font  # размер шрифта
        self.width = width  # ширина кнопки
        self.master = master
        self.button = Button(master=master, text=self.text, font=self.font, command=command)  # Добавлен command
        self.button.place(x=self.x, y=self.y, width=self.width)


if __name__ == "__main__":
    window = MyWindow()