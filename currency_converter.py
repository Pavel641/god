import tkinter as tk
from tkinter import messagebox, ttk

class CurrencyConverter:
    def __init__(self, parent):
        self.parent = parent
        self.win = tk.Toplevel(parent)
        self.win.title('💰 Конвертер валют')
        self.win.geometry('400x350')
        self.win.configure(bg='#f0f0f0')
        
        self.rates = {
            'RUB': 1,
            'USD': 0.011,
            'EUR': 0.010,
            'CNY': 0.079,
            'GBP': 0.0087,
            'JPY': 1.65,
            'KZT': 5.25,
            'UAH': 0.45
        }
        
        tk.Label(self.win, text='Конвертер валют', font=('Segoe UI', 18, 'bold'), bg='#f0f0f0').pack(pady=15)
        
        frame_from = tk.Frame(self.win, bg='#f0f0f0')
        frame_from.pack(pady=10)
        tk.Label(frame_from, text='Из:', font=('Segoe UI', 12), bg='#f0f0f0').pack(side='left', padx=10)
        self.from_currency = ttk.Combobox(frame_from, values=list(self.rates.keys()), width=10)
        self.from_currency.pack(side='left')
        self.from_currency.set('RUB')
        
        frame_to = tk.Frame(self.win, bg='#f0f0f0')
        frame_to.pack(pady=10)
        tk.Label(frame_to, text='В:', font=('Segoe UI', 12), bg='#f0f0f0').pack(side='left', padx=10)
        self.to_currency = ttk.Combobox(frame_to, values=list(self.rates.keys()), width=10)
        self.to_currency.pack(side='left')
        self.to_currency.set('USD')
        
        frame_amount = tk.Frame(self.win, bg='#f0f0f0')
        frame_amount.pack(pady=10)
        tk.Label(frame_amount, text='Сумма:', font=('Segoe UI', 12), bg='#f0f0f0').pack(side='left', padx=10)
        self.amount_entry = tk.Entry(frame_amount, width=15, font=('Segoe UI', 11))
        self.amount_entry.pack(side='left')
        
        self.result_label = tk.Label(self.win, text='', font=('Segoe UI', 14, 'bold'), bg='#f0f0f0', fg='#2ecc71')
        self.result_label.pack(pady=20)
        
        tk.Button(self.win, text='🔄 Конвертировать', command=self.convert, bg='#2ecc71', fg='white', font=('Segoe UI', 12), width=20, height=2).pack(pady=20)
    
    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            
            rub_amount = amount / self.rates[from_curr]
            result = rub_amount * self.rates[to_curr]
            
            self.result_label.config(text=f'{amount} {from_curr} = {result:.2f} {to_curr}')
        except ValueError:
            messagebox.showwarning('Ошибка', 'Введите корректную сумму!')

def currency_converter(parent):
    CurrencyConverter(parent)
