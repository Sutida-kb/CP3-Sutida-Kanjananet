from forex_python.converter import CurrencyRates
from tkinter import *
from tkinter import ttk
import datetime

c = CurrencyRates()
c.get_rates('USD')
first_currency = " "
target_currency = " "

def obtener():
    choose_exchange_list =[combo.get(),combo2.get()]
    first_currency = choose_exchange_list[0]
    target_currency = choose_exchange_list[1]
    print(first_currency,"can exchange to",target_currency)
    print("-"*20)
    month_currency: list[float] = []
    sum_month = 0
    for i in range(30):
        i += 1
        old_date = datetime.datetime.now() - datetime.timedelta(i)
        previous_currency = c.get_rate(first_currency, target_currency, old_date)
        month_currency.append(float(previous_currency))
        sum_month += previous_currency
    print("-" * 20)
    print("  ")
    print("Calculated date and time is", datetime.datetime.now())
    print(first_currency, "can exchange to", c.get_rate(first_currency, target_currency, datetime.datetime.now()),
          target_currency)
    print("  ")
    print("Min in month ::", min(month_currency), target_currency)
    print("Max in month ::", max(month_currency), target_currency)
    print("Average in month ::", sum_month / 30, target_currency)
    print("  ")


mainwindows = Tk()

textch = Label(mainwindows, text="first_currency").grid(row=0, column=0)
combo = ttk.Combobox(mainwindows)
textch2 = Label(mainwindows, text="target_currency").grid(row=0, column=1)
combo = ttk.Combobox(mainwindows)
combo.grid(row=1, column=0)
combo['values'] = list(c.get_rates("").keys())
combo.current(0)
combo2 = ttk.Combobox(mainwindows)
combo2.grid(row=1, column=1)
combo2['values'] = list(c.get_rates("").keys())
combo2.current(0)
submit = Button(mainwindows, command=obtener, text="Calcular").grid(row=4, column=0)

mainwindows.geometry("300x300")
mainwindows.mainloop()

