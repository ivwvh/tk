import tkinter as tk
from tkinter import ttk
import requests


def change_label_text(label: ttk.Label, text: str) -> None:
    label['text'] = text


# создаем элементы
window = tk.Tk()
label = ttk.Label(master=window, text='Сколько у вас рублей?')
user_rub_entry = ttk.Entry(window)

usd_label = ttk.Label(window, text='')
eur_label = ttk.Label(window, text='')
yuan_label = ttk.Label(window, text='')

convert_to_usd_button = ttk.Button(window, text='Перевести в доллары',
                                   command=lambda: change_label_text(usd_label,
                                                                     text=f'У ваc: {round(float(user_rub_entry.get()) / 97, 2)} долларов'))
convert_to_euro_button = ttk.Button(window, text='Перевести в евро',
                                    command=lambda: change_label_text(eur_label,
                                                                      text=f'У ваc: {round(float(user_rub_entry.get()) / 104, 2)} евро'))
convert_to_yuan_button = ttk.Button(window, text='Перевести в юани',
                                    command=lambda: change_label_text(yuan_label,
                                                                      text=f'У ваc: {round(float(user_rub_entry.get()) / 13, 2)} юань'))

# настраиваем элементы
window.geometry('800x600+0+0')  # разрешение + отступX + отступY

# выводим элементы

label.pack()
user_rub_entry.pack()
convert_to_usd_button.pack()
convert_to_euro_button.pack()
convert_to_yuan_button.pack()
usd_label.pack()
eur_label.pack()
yuan_label.pack()

window.mainloop()
