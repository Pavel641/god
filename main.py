import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import json


class FourInOneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Утилита 4 в 1")
        self.root.geometry("600x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        title_font = ("Segoe UI", 22, "bold")
        btn_font = ("Segoe UI", 12)

        tk.Label(root, text="🛠️ Утилита 4 в 1", font=title_font, bg="#f0f0f0", fg="#333").pack(pady=20)

        btn_style = {"width": 35, "height": 2, "font": btn_font, "relief": "raised", "bd": 2}

        tk.Button(root, text="📝 1. Планировщик задач", command=self.task_planner,
                  bg="#3498db", fg="white", **btn_style).pack(pady=5)

        tk.Button(root, text="💰 2. Конвертер валют", command=self.currency_converter,
                  bg="#2ecc71", fg="white", **btn_style).pack(pady=5)

        tk.Button(root, text="🎲 3. Генератор случайных чисел", command=self.random_number,
                  bg="#e67e22", fg="white", **btn_style).pack(pady=5)

        tk.Button(root, text="🔐 4. Менеджер паролей", command=self.password_manager,
                  bg="#9b59b6", fg="white", **btn_style).pack(pady=5)

        tk.Button(root, text="❌ Выход", command=root.quit,
                  bg="#e74c3c", fg="white", **btn_style).pack(pady=30)

    def task_planner(self):
        win = tk.Toplevel(self.root)
        win.title("📝 Планировщик задач")
        win.geometry("500x550")
        win.configure(bg="#f0f0f0")

        tk.Label(win, text="Мои задачи", font=("Segoe UI", 18, "bold"), bg="#f0f0f0").pack(pady=10)

        frame_add = tk.Frame(win, bg="#f0f0f0")
        frame_add.pack(pady=10)

        task_entry = tk.Entry(frame_add, width=35, font=("Segoe UI", 11))
        task_entry.pack(side="left", padx=5)

        def add_task():
            task = task_entry.get().strip()
            if task:
                listbox.insert(tk.END, task)
                task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Ошибка", "Введите задачу!")

        tk.Button(frame_add, text="➕ Добавить", command=add_task, bg="#3498db", fg="white").pack(side="left")

        listbox = tk.Listbox(win, width=50, height=15, font=("Segoe UI", 11), selectmode=tk.SINGLE)
        listbox.pack(pady=10)

        frame_buttons = tk.Frame(win, bg="#f0f0f0")
        frame_buttons.pack(pady=5)

        def delete_task():
            selected = listbox.curselection()
            if selected:
                listbox.delete(selected)

        def complete_task():
            selected = listbox.curselection()
            if selected:
                task = listbox.get(selected)
                if not task.startswith("✅"):
                    listbox.delete(selected)
                    listbox.insert(tk.END, f"✅ {task}")

        tk.Button(frame_buttons, text="❌ Удалить", command=delete_task, bg="#e74c3c", fg="white", width=12).pack(
            side="left", padx=5)
        tk.Button(frame_buttons, text="✔️ Выполнено", command=complete_task, bg="#2ecc71", fg="white", width=12).pack(
            side="left", padx=5)

        def save_tasks():
            tasks = listbox.get(0, tk.END)
            with open("tasks.json", "w", encoding="utf-8") as f:
                json.dump(list(tasks), f, ensure_ascii=False)
            messagebox.showinfo("Успех", "Задачи сохранены!")

        def load_tasks():
            try:
                with open("tasks.json", "r", encoding="utf-8") as f:
                    tasks = json.load(f)
                    for task in tasks:
                        listbox.insert(tk.END, task)
            except FileNotFoundError:
                pass

        frame_save_load = tk.Frame(win, bg="#f0f0f0")
        frame_save_load.pack(pady=10)

        tk.Button(frame_save_load, text="💾 Сохранить", command=save_tasks, bg="#3498db", fg="white", width=15).pack(
            side="left", padx=5)
        tk.Button(frame_save_load, text="📂 Загрузить", command=load_tasks, bg="#9b59b6", fg="white", width=15).pack(
            side="left", padx=5)

        load_tasks()

    def currency_converter(self):
        win = tk.Toplevel(self.root)
        win.title("💰 Конвертер валют")
        win.geometry("400x350")
        win.configure(bg="#f0f0f0")

        rates = {
            "RUB": 1,
            "USD": 0.011,
            "EUR": 0.010,
            "CNY": 0.079,
            "GBP": 0.0087,
            "JPY": 1.65,
            "KZT": 5.25,
            "UAH": 0.45
        }

        tk.Label(win, text="Конвертер валют", font=("Segoe UI", 18, "bold"), bg="#f0f0f0").pack(pady=15)

        frame_from = tk.Frame(win, bg="#f0f0f0")
        frame_from.pack(pady=10)
        tk.Label(frame_from, text="Из:", font=("Segoe UI", 12), bg="#f0f0f0").pack(side="left", padx=10)
        from_currency = ttk.Combobox(frame_from, values=list(rates.keys()), width=10)
        from_currency.pack(side="left")
        from_currency.set("RUB")

        frame_to = tk.Frame(win, bg="#f0f0f0")
        frame_to.pack(pady=10)
        tk.Label(frame_to, text="В:", font=("Segoe UI", 12), bg="#f0f0f0").pack(side="left", padx=10)
        to_currency = ttk.Combobox(frame_to, values=list(rates.keys()), width=10)
        to_currency.pack(side="left")
        to_currency.set("USD")

        frame_amount = tk.Frame(win, bg="#f0f0f0")
        frame_amount.pack(pady=10)
        tk.Label(frame_amount, text="Сумма:", font=("Segoe UI", 12), bg="#f0f0f0").pack(side="left", padx=10)
        amount_entry = tk.Entry(frame_amount, width=15, font=("Segoe UI", 11))
        amount_entry.pack(side="left")

        result_label = tk.Label(win, text="", font=("Segoe UI", 14, "bold"), bg="#f0f0f0", fg="#2ecc71")
        result_label.pack(pady=20)

        def convert():
            try:
                amount = float(amount_entry.get())
                from_curr = from_currency.get()
                to_curr = to_currency.get()

                rub_amount = amount / rates[from_curr]
                result = rub_amount * rates[to_curr]

                result_label.config(text=f"{amount} {from_curr} = {result:.2f} {to_curr}")
            except ValueError:
                messagebox.showwarning("Ошибка", "Введите корректную сумму!")

        tk.Button(win, text="🔄 Конвертировать", command=convert, bg="#2ecc71", fg="white", font=("Segoe UI", 12),
                  width=20, height=2).pack(pady=20)

    def random_number(self):
        win = tk.Toplevel(self.root)
        win.title("🎲 Генератор случайных чисел")
        win.geometry("450x450")
        win.configure(bg="#f0f0f0")

        tk.Label(win, text="Генератор случайных чисел", font=("Segoe UI", 18, "bold"), bg="#f0f0f0").pack(pady=15)

        frame_min = tk.Frame(win, bg="#f0f0f0")
        frame_min.pack(pady=10)
        tk.Label(frame_min, text="Минимум:", font=("Segoe UI", 12), bg="#f0f0f0").pack(side="left", padx=10)
        min_entry = tk.Entry(frame_min, width=15, font=("Segoe UI", 11))
        min_entry.pack(side="left")
        min_entry.insert(0, "1")

        frame_max = tk.Frame(win, bg="#f0f0f0")
        frame_max.pack(pady=10)
        tk.Label(frame_max, text="Максимум:", font=("Segoe UI", 12), bg="#f0f0f0").pack(side="left", padx=10)
        max_entry = tk.Entry(frame_max, width=15, font=("Segoe UI", 11))
        max_entry.pack(side="left")
        max_entry.insert(0, "100")

        result_label = tk.Label(win, text="", font=("Segoe UI", 24, "bold"), bg="#f0f0f0", fg="#e67e22")
        result_label.pack(pady=30)

        def generate():
            try:
                min_val = int(min_entry.get())
                max_val = int(max_entry.get())

                if min_val > max_val:
                    messagebox.showwarning("Ошибка", "Минимум не может быть больше максимума!")
                    return

                number = random.randint(min_val, max_val)
                result_label.config(text=str(number))

            except ValueError:
                messagebox.showwarning("Ошибка", "Введите корректные числа!")

        def generate_multiple():
            try:
                min_val = int(min_entry.get())
                max_val = int(max_entry.get())

                if min_val > max_val:
                    messagebox.showwarning("Ошибка", "Минимум не может быть больше максимума!")
                    return

                numbers = [random.randint(min_val, max_val) for _ in range(5)]
                result_label.config(text=", ".join(map(str, numbers)))

            except ValueError:
                messagebox.showwarning("Ошибка", "Введите корректные числа!")

        btn_frame = tk.Frame(win, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="🎲 Одно число", command=generate, bg="#e67e22", fg="white", font=("Segoe UI", 12),
                  width=15, height=2).pack(side="left", padx=10)
        tk.Button(btn_frame, text="🎲 5 чисел", command=generate_multiple, bg="#3498db", fg="white",
                  font=("Segoe UI", 12), width=15, height=2).pack(side="left", padx=10)

    def password_manager(self):
        win = tk.Toplevel(self.root)
        win.title("🔐 Менеджер паролей")
        win.geometry("600x500")
        win.configure(bg="#f0f0f0")

        notebook = ttk.Notebook(win)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        frame_generator = tk.Frame(notebook, bg="#f0f0f0")
        frame_storage = tk.Frame(notebook, bg="#f0f0f0")

        notebook.add(frame_generator, text="Генератор паролей")
        notebook.add(frame_storage, text="Хранилище паролей")

        length_var = tk.IntVar(value=12)
        use_upper = tk.BooleanVar(value=True)
        use_lower = tk.BooleanVar(value=True)
        use_digits = tk.BooleanVar(value=True)
        use_symbols = tk.BooleanVar(value=True)

        tk.Label(frame_generator, text="Генератор паролей", font=("Segoe UI", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        tk.Label(frame_generator, text="Длина пароля:", bg="#f0f0f0").pack()
        length_scale = tk.Scale(frame_generator, from_=4, to=32, orient=tk.HORIZONTAL, variable=length_var, length=300,
                                bg="#f0f0f0")
        length_scale.pack()

        tk.Checkbutton(frame_generator, text="Заглавные буквы (A-Z)", variable=use_upper, bg="#f0f0f0").pack()
        tk.Checkbutton(frame_generator, text="Строчные буквы (a-z)", variable=use_lower, bg="#f0f0f0").pack()
        tk.Checkbutton(frame_generator, text="Цифры (0-9)", variable=use_digits, bg="#f0f0f0").pack()
        tk.Checkbutton(frame_generator, text="Символы (!@#$%^&*)", variable=use_symbols, bg="#f0f0f0").pack()

        password_display = tk.Entry(frame_generator, font=("Courier", 14), width=30)
        password_display.pack(pady=10)

        def generate_password():
            chars = ""
            if use_upper.get():
                chars += string.ascii_uppercase
            if use_lower.get():
                chars += string.ascii_lowercase
            if use_digits.get():
                chars += string.digits
            if use_symbols.get():
                chars += "!@#$%^&*"

            if not chars:
                messagebox.showwarning("Ошибка", "Выберите хотя бы один тип символов!")
                return

            length = length_var.get()
            password = ''.join(random.choice(chars) for _ in range(length))
            password_display.delete(0, tk.END)
            password_display.insert(0, password)

        def copy_password():
            password = password_display.get()
            if password:
                win.clipboard_clear()
                win.clipboard_append(password)
                messagebox.showinfo("Успех", "Пароль скопирован!")

        tk.Button(frame_generator, text="🔐 Сгенерировать", command=generate_password, bg="#9b59b6", fg="white",
                  width=20).pack(pady=5)
        tk.Button(frame_generator, text="📋 Скопировать", command=copy_password, bg="#3498db", fg="white",
                  width=20).pack()

        tk.Label(frame_storage, text="Хранилище паролей", font=("Segoe UI", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        frame_service = tk.Frame(frame_storage, bg="#f0f0f0")
        frame_service.pack(pady=10)

        tk.Label(frame_service, text="Сервис/Сайт:", bg="#f0f0f0").pack(side="left", padx=5)
        service_entry = tk.Entry(frame_service, width=20)
        service_entry.pack(side="left", padx=5)

        tk.Label(frame_service, text="Пароль:", bg="#f0f0f0").pack(side="left", padx=5)
        pass_entry = tk.Entry(frame_service, width=20)
        pass_entry.pack(side="left", padx=5)

        passwords_list = tk.Listbox(frame_storage, width=60, height=12, font=("Segoe UI", 10))
        passwords_list.pack(pady=10)

        def load_passwords():
            try:
                with open("passwords.json", "r") as f:
                    passwords = json.load(f)
                    for service, pwd in passwords.items():
                        passwords_list.insert(tk.END, f"{service}: {pwd}")
            except FileNotFoundError:
                pass

        def save_password():
            service = service_entry.get().strip()
            password = pass_entry.get().strip()

            if not service or not password:
                messagebox.showwarning("Ошибка", "Заполните оба поля!")
                return

            try:
                with open("passwords.json", "r") as f:
                    passwords = json.load(f)
            except FileNotFoundError:
                passwords = {}

            passwords[service] = password

            with open("passwords.json", "w") as f:
                json.dump(passwords, f, ensure_ascii=False, indent=2)

            passwords_list.insert(tk.END, f"{service}: {password}")
            service_entry.delete(0, tk.END)
            pass_entry.delete(0, tk.END)
            messagebox.showinfo("Успех", "Пароль сохранён!")

        def delete_password():
            selected = passwords_list.curselection()
            if selected:
                item = passwords_list.get(selected)
                service = item.split(":")[0]

                with open("passwords.json", "r") as f:
                    passwords = json.load(f)

                if service in passwords:
                    del passwords[service]

                with open("passwords.json", "w") as f:
                    json.dump(passwords, f, ensure_ascii=False, indent=2)

                passwords_list.delete(selected)
                messagebox.showinfo("Успех", "Пароль удалён!")

        tk.Button(frame_storage, text="💾 Сохранить пароль", command=save_password, bg="#2ecc71", fg="white",
                  width=20).pack(pady=5)
        tk.Button(frame_storage, text="🗑️ Удалить пароль", command=delete_password, bg="#e74c3c", fg="white",
                  width=20).pack()

        load_passwords()


if __name__ == "__main__":
    root = tk.Tk()
    app = FourInOneApp(root)
    root.mainloop()