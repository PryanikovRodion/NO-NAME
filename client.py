import tkinter as tk
from saler import Saler
from buyer import Buyer
from product import Product
from magazin import Magazin
import threading

WIDTH = 400
HEIGHT = 300
PADX = 16
PADY = 12
FONT_1 = ("Bauhaus 93", 48)
FONT_2 = ("Times New Roman", 24)
FONT_3 = ("Courier New", 24)
FONT_4 = ("Goudy Old Style", 24)

def create_main_window():
    """Создает главное окно."""
    root = tk.Tk()
    root.title("Start Window")
    root.geometry(f"{WIDTH}x{HEIGHT}")

    btn_login = tk.Button(master=root, text="login", font=FONT_3, command=lambda: on_login(root))
    btn_login.pack(expand=True, fill="both", padx=PADX, pady=PADY)

    btn_logout = tk.Button(master=root, text="logout", font=FONT_3, command=lambda: on_logout(root))
    btn_logout.pack(expand=True, fill="both", padx=PADX, pady=PADY)

    root.mainloop()

def on_login(root):
    """Обработчик кнопки login."""
    print("login")

def on_logout(root):
    """Обработчик кнопки logout."""
    root.destroy()
    new_root = tk.Tk()
    new_root.title("Выбор роли")
    new_root.geometry(f"{WIDTH}x{HEIGHT}")

    btn_saler = tk.Button(master=new_root, text="Saler", font=FONT_4, command=lambda: open_saler_register_window(new_root))
    btn_saler.pack(expand=True, fill="both", padx=PADX, pady=PADY)

    btn_buyer = tk.Button(master=new_root, text="Buyer", font=FONT_4, command=lambda: open_buyer_register_window(new_root))
    btn_buyer.pack(expand=True, fill="both", padx=PADX, pady=PADY)

    new_root.mainloop()

def open_saler_register_window(parent):
    """Открывает окно регистрации продавца."""
    parent.destroy()
    reg_root = tk.Tk()
    reg_root.title("Регистрация продавца")
    reg_root.geometry(f"{WIDTH}x{HEIGHT}")

    tk.Label(reg_root, text="Имя пользователя:").pack()
    username_entry = tk.Entry(reg_root)
    username_entry.pack()

    tk.Label(reg_root, text="Пароль:").pack()
    password_entry = tk.Entry(reg_root, show="*")
    password_entry.pack()

    tk.Label(reg_root, text="Подтвердите пароль:").pack()
    confirm_password_entry = tk.Entry(reg_root, show="*")
    confirm_password_entry.pack()

    register_button = tk.Button(reg_root, text="Зарегистрироваться",
                                command=lambda: on_register(username_entry, password_entry, confirm_password_entry))
    register_button.pack()

    reg_root.mainloop()
    

def open_buyer_register_window(parent):
    """Открывает окно регистрации покупателя."""
    parent.destroy()
    reg_root = tk.Tk()
    reg_root.title("Регистрация покупателя")
    reg_root.geometry(f"{WIDTH}x{HEIGHT}")

    tk.Label(reg_root, text="Имя пользователя:").pack()
    username_entry = tk.Entry(reg_root)
    username_entry.pack()

    tk.Label(reg_root, text="Пароль:").pack()
    password_entry = tk.Entry(reg_root, show="*")
    password_entry.pack()

    tk.Label(reg_root, text="Подтвердите пароль:").pack()
    confirm_password_entry = tk.Entry(reg_root, show="*")
    confirm_password_entry.pack()

    register_button = tk.Button(reg_root, text="Зарегистрироваться",
                                command=lambda: on_register(username_entry, password_entry, confirm_password_entry))
    register_button.pack()

    reg_root.mainloop()


def on_register(username_entry, password_entry, confirm_password_entry):
    """Обработчик регистрации."""
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if password == confirm_password:
        print(f"Регистрация успешна! Имя: {username}, Пароль: {password}")
    else:
        print("Пароли не совпадают!")

if __name__ == "__main__":
    create_main_window()
