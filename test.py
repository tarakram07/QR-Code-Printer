import tkinter as tk
from tkinter import ttk

def select_option(event):
    selected_option = dropdown.get()

    if selected_option == "Option 1":
        entry1.delete(0, tk.END)
        entry1.insert(tk.END, "Wert für Option 1")
        entry2.delete(0, tk.END)
        entry2.insert(tk.END, "Weitere Werte für Option 1")
    elif selected_option == "Option 2":
        entry1.delete(0, tk.END)
        entry1.insert(tk.END, "Wert für Option 2")
        entry2.delete(0, tk.END)
        entry2.insert(tk.END, "Weitere Werte für Option 2")
    elif selected_option == "Option 3":
        entry1.delete(0, tk.END)
        entry1.insert(tk.END, "Wert für Option 3")
        entry2.delete(0, tk.END)
        entry2.insert(tk.END, "Weitere Werte für Option 3")

root = tk.Tk()

# Erstelle ein OptionMenu-Widget
dropdown = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
dropdown.pack()
dropdown.bind("<<ComboboxSelected>>", select_option)

# Erstelle Eingabefelder
entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

root.mainloop()
