import tkinter as tk
from tkinter import messagebox
import random

class RandomNumber:
    def __init__(self, parent):
        self.parent = parent
        self.win = tk.Toplevel(parent)
        self.win.title('🎲 Генератор случайных чисел')
        self.win.geometry('450x450')
        self.win.configure(bg='#f0f0f0')
        
        tk.Label(self.win, text='Генератор случайных чисел', font=('Segoe UI', 18, 'bold'), bg='#f0f0f0').pack(pady=15)
        
        frame_min = tk.Frame(self.win, bg='#f0f0f0')
        frame_min.pack(pady=10)
        tk.Label(frame_min, text='Минимум:', font=('Segoe UI', 12), bg='#f0f0f0').pack(side='left', padx=10)
        self.min_entry = tk.Entry(frame_min, width=15, font=('Segoe UI', 11))
        self.min_entry.pack(side='left')
        self.min_entry.insert(0, '1')
        
        frame_max = tk.Frame(self.win, bg='#f0f0f0')
        frame_max.pack(pady=10)
        tk.Label(frame_max, text='Максимум:', font=('Segoe UI', 12), bg='#f0f0f0').pack(side='left', padx=10)
        self.max_entry = tk.Entry(frame_max, width=15, font=('Segoe UI', 11))
        self.max_entry.pack(side='left')
        self.max_entry.insert(0, '100')
        
        self.result_label = tk.Label(self.win, text='', font=('Segoe UI', 24, 'bold'), bg='#f0f0f0', fg='#e67e22')
        self.result_label.pack(pady=30)
        
        btn_frame = tk.Frame(self.win, bg='#f0f0f0')
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text='🎲 Одно число', command=self.generate_one, bg='#e67e22', fg='white', font=('Segoe UI', 12), width=15, height=2).pack(side='left', padx=10)
        tk.Button(btn_frame, text='🎲 5 чисел', command=self.generate_five, bg='#3498db', fg='white', font=('Segoe UI', 12), width=15, height=2).pack(side='left', padx=10)
    
    def generate_one(self):
        try:
            min_val = int(self.min_entry.get())
            max_val = int(self.max_entry.get())
            
            if min_val > max_val:
                messagebox.showwarning('Ошибка', 'Минимум не может быть больше максимума!')
                return
            
            number = random.randint(min_val, max_val)
            self.result_label.config(text=str(number))
        except ValueError:
            messagebox.showwarning('Ошибка', 'Введите корректные числа!')
    
    def generate_five(self):
        try:
            min_val = int(self.min_entry.get())
            max_val = int(self.max_entry.get())
            
            if min_val > max_val:
                messagebox.showwarning('Ошибка', 'Минимум не может быть больше максимума!')
                return
            
            numbers = [random.randint(min_val, max_val) for _ in range(5)]
            self.result_label.config(text=', '.join(map(str, numbers)))
        except ValueError:
            messagebox.showwarning('Ошибка', 'Введите корректные числа!')

def random_number(parent):
    RandomNumber(parent)
