import tkinter as tk
from tkinter import messagebox
import json

class TaskPlanner:
    def __init__(self, parent):
        self.parent = parent
        self.win = tk.Toplevel(parent)
        self.win.title('📝 Планировщик задач')
        self.win.geometry('500x550')
        self.win.configure(bg='#f0f0f0')
        
        tk.Label(self.win, text='Мои задачи', font=('Segoe UI', 18, 'bold'), bg='#f0f0f0').pack(pady=10)
        
        frame_add = tk.Frame(self.win, bg='#f0f0f0')
        frame_add.pack(pady=10)
        
        self.task_entry = tk.Entry(frame_add, width=35, font=('Segoe UI', 11))
        self.task_entry.pack(side='left', padx=5)
        
        tk.Button(frame_add, text='➕ Добавить', command=self.add_task, bg='#3498db', fg='white').pack(side='left')
        
        self.listbox = tk.Listbox(self.win, width=50, height=15, font=('Segoe UI', 11), selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)
        
        frame_buttons = tk.Frame(self.win, bg='#f0f0f0')
        frame_buttons.pack(pady=5)
        
        tk.Button(frame_buttons, text='❌ Удалить', command=self.delete_task, bg='#e74c3c', fg='white', width=12).pack(side='left', padx=5)
        tk.Button(frame_buttons, text='✔️ Выполнено', command=self.complete_task, bg='#2ecc71', fg='white', width=12).pack(side='left', padx=5)
        
        frame_save_load = tk.Frame(self.win, bg='#f0f0f0')
        frame_save_load.pack(pady=10)
        
        tk.Button(frame_save_load, text='💾 Сохранить', command=self.save_tasks, bg='#3498db', fg='white', width=15).pack(side='left', padx=5)
        tk.Button(frame_save_load, text='📂 Загрузить', command=self.load_tasks, bg='#9b59b6', fg='white', width=15).pack(side='left', padx=5)
        
        self.load_tasks()
    
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning('Ошибка', 'Введите задачу!')
    
    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
    
    def complete_task(self):
        selected = self.listbox.curselection()
        if selected:
            task = self.listbox.get(selected)
            if not task.startswith('✅'):
                self.listbox.delete(selected)
                self.listbox.insert(tk.END, f'✅ {task}')
    
    def save_tasks(self):
        tasks = self.listbox.get(0, tk.END)
        with open('tasks.json', 'w', encoding='utf-8') as f:
            json.dump(list(tasks), f, ensure_ascii=False)
        messagebox.showinfo('Успех', 'Задачи сохранены!')
    
    def load_tasks(self):
        try:
            with open('tasks.json', 'r', encoding='utf-8') as f:
                tasks = json.load(f)
                for task in tasks:
                    self.listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

def task_planner(parent):
    TaskPlanner(parent)
