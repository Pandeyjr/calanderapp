import tkinter as tk
import calendar
from tkinter import ttk

def show_calendar():
    year = int(year_entry.get())
    month = int(month_entry.get())
    cal = calendar.month(year, month)
    cal_display.config(state='normal')
    cal_display.delete(1.0, tk.END)
    cal_display.insert(tk.END, cal)
    cal_display.config(state='disabled')

# Create the main window
root = tk.Tk()
root.title("Simple Calendar")

# Input fields for year and month
year_label = ttk.Label(root, text="Year:")
year_label.grid(row=0, column=0)
year_entry = ttk.Entry(root)
year_entry.grid(row=0, column=1)

month_label = ttk.Label(root, text="Month:")
month_label.grid(row=1, column=0)
month_entry = ttk.Entry(root)
month_entry.grid(row=1, column=1)

# Button to display the calendar
cal_button = ttk.Button(root, text="Show Calendar", command=show_calendar)
cal_button.grid(row=2, column=0, columnspan=2)

# Text widget to display the calendar
cal_display = tk.Text(root, width=20, height=8, state='disabled')
cal_display.grid(row=3, column=0, columnspan=2)

root.mainloop()
