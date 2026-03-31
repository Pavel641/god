import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import json

class PasswordManager:
    def __init__(self, parent):
        self.parent = parent
        self.win = tk.Toplevel(parent)
        self.win.title('🔐 Менеджер паролей')
        self.win.geometry('600x500')
        self.win.configure(bg='#f0f0f0')
        
        notebook = ttk.Notebook(self.win)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        frame_generator = tk.Frame(notebook, bg='#f0f0f0')
        frame_storage = tk.Frame(notebook, bg='#f0f0f0')
        
        notebook.add(frame_generator, text='Генератор паролей')
        notebook.add(frame_storage, text='Хранилище паролей')
        
        self.length_var = tk.IntVar(value=12)
        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        
        tk.Label(frame_generator, text='Генератор паролей', font=('Segoe UI', 16, 'bold'), bg='#f0f0f0').pack(pady=10)
        
        tk.Label(frame_generator, text='Длина пароля:', bg='#f0f0f0').pack()
        length_scale = tk.Scale(frame_generator, from_=4, to=32, orient=tk.HORIZONTAL, variable=self.length_var, length=300, bg='#f0f0f0')
        length_scale.pack()
        
        tk.Checkbutton(frame_generator, text='Заглавные буквы (A-Z)', variable=self.use_upper, bg='#f0f0f0').pack()
        tk.Checkbutton(frame_generator, text='Строчные буквы (a-z)', variable=self.use_lower, bg='#f0f0f0').pack()
        tk.Checkbutton(frame_generator, text='Цифры (0-9)', variable=self.use_digits, bg='#f0f0f0').pack()
        tk.Checkbutton(frame_generator, text='Символы (!@#$%^&*)', variable=self.use_symbols, bg='#f0f0f0').pack()
        
        self.password_display = tk.Entry(frame_generator, font=('Courier', 14), width=30)
        self.password_display.pack(pady=10)
        
        tk.Button(frame_generator, text='🔐 Сгенерировать', command=self.generate_password, bg='#9b59b6', fg='white', width=20).pack(pady=5)
        tk.Button(frame_generator, text='📋 Скопировать', command=self.copy_password, bg='#3498db', fg='white', width=20).pack()
        
        tk.Label(frame_storage, text='Хранилище паролей', font=('Segoe UI', 16, 'bold'), bg='#f0f0f0').pack(pady=10)
        
        frame_service = tk.Frame(frame_storage, bg='#f0f0f0')
        frame_service.pack(pady=10)
        
        tk.Label(frame_service, text='Сервис/Сайт:', bg='#f0f0f0').pack(side='left', padx=5)
        self.service_entry = tk.Entry(frame_service, width=20)
        self.service_entry.pack(side='left', padx=5)
        
        tk.Label(frame_service, text='Пароль:', bg='#f0f0f0').pack(side='left', padx=5)
        self.pass_entry = tk.Entry(frame_service, width=20)
        self.pass_entry.pack(side='left', padx=5)
        
        self.passwords_list = tk.Listbox(frame_storage, width=60, height=12, font=('Segoe UI', 10))
        self.passwords_list.pack(pady=10)
        
        tk.Button(frame_storage, text='💾 Сохранить пароль', command=self.save_password, bg='#2ecc71', fg='white', width=20).pack(pady=5)
        tk.Button(frame_storage, text='🗑️ Удалить пароль', command=self.delete_password, bg='#e74c3c', fg='white', width=20).pack()
        
        self.load_passwords()
    
    def generate_password(self):
        chars = ''
        if self.use_upper.get():
            chars += string.ascii_uppercase
        if self.use_lower.get():
            chars += string.ascii_lowercase
        if self.use_digits.get():
            chars += string.digits
        if self.use_symbols.get():
            chars += '!@#$%^&*'
        
        if not chars:
            messagebox.showwarning('Ошибка', 'Выберите хотя бы один тип символов!')
            return
        
        length = self.length_var.get()
        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)
    
    def copy_password(self):
        password = self.password_display.get()
        if password:
            self.win.clipboard_clear()
            self.win.clipboard_append(password)
            messagebox.showinfo('Успех', 'Пароль скопирован!')
    
    def load_passwords(self):
        try:
            with open('passwords.json', 'r') as f:
                passwords = json.load(f)
                for service, pwd in passwords.items():
                    self.passwords_list.insert(tk.END, f'{service}: {pwd}')
        except FileNotFoundError:
            pass
    
    def save_password(self):
        service = self.service_entry.get().strip()
        password = self.pass_entry.get().strip()
        
        if not service or not password:
            messagebox.showwarning('Ошибка', 'Заполните оба поля!')
            return
        
        try:
            with open('passwords.json', 'r') as f:
                passwords = json.load(f)
        except FileNotFoundError:
            passwords = {}
        
        passwords[service] = password
        
        with open('passwords.json', 'w') as f:
            json.dump(passwords, f, ensure_ascii=False, indent=2)
        
        self.passwords_list.insert(tk.END, f'{service}: {password}')
        self.service_entry.delete(0, tk.END)
        self.pass_entry.delete(0, tk.END)
        messagebox.showinfo('Успех', 'Пароль сохранён!')
    
    def delete_password(self):
        selected = self.passwords_list.curselection()
        if selected:
            item = self.passwords_list.get(selected)
            service = item.split(':')[0]
            
            with open('passwords.json', 'r') as f:
                passwords = json.load(f)
            
            if service in passwords:
                del passwords[service]
            
            with open('passwords.json', 'w') as f:
                json.dump(passwords, f, ensure_ascii=False, indent=2)
            
            self.passwords_list.delete(selected)
            messagebox.showinfo('Успех', 'Пароль удалён!')

def password_manager(parent):
    PasswordManager(parent)
