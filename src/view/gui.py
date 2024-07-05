import tkinter as tk
from tkinter import ttk

def create_data_display_gui(data):
    root = tk.Tk()
    root.title("Financial Market Weekly Stats")

    # Create a Treeview
    tree = ttk.Treeview(root)
    tree["columns"] = ("Positive Days (%)", "Negative Days (%)")
    tree.column("#0", width=100, minwidth=50)
    tree.column("Positive Days (%)", width=100, minwidth=50)
    tree.column("Negative Days (%)", width=100, minwidth=50)

    tree.heading("#0", text="Day of Week", anchor=tk.W)
    tree.heading("Positive Days (%)", text="Positive Days (%)", anchor=tk.W)
    tree.heading("Negative Days (%)", text="Negative Days (%)", anchor=tk.W)

    # Insert the data into the Treeview
    for index, row in data.iterrows():
        tree.insert("", "end", text=index, values=(round(row['Positive Days (%)'], 2), round(row['Negative Days (%)'], 2)))

    tree.pack(side=tk.TOP, fill=tk.X)

    # Run the GUI
    root.mainloop()