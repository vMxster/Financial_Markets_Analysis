import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from view.gui import create_data_display_gui
from model.loader import load_and_process_data

def create_market_selection_gui():
    def on_market_selected():
        market = market_var.get()
        if market == "Select a market":
            messagebox.showwarning("Selection Error", "Please select a valid market.")
        else:
            file_path = f'./Data/{market}_Historical_Data.csv'
            try:
                data = load_and_process_data(file_path)
                root.destroy()
                create_data_display_gui(data)
            except FileNotFoundError:
                messagebox.showerror("File Error", f"The file for {market} was not found.")
    
    root = tk.Tk()
    root.title("Welcome")

    tk.Label(root, text="Select Financial Market").pack(pady=10)

    market_var = tk.StringVar(root)
    market_var.set("Select a market")
    markets = ["SP500", "NASDAQ", "EUR"]

    market_menu = ttk.OptionMenu(root, market_var, *markets)
    market_menu.pack(pady=10)

    tk.Button(root, text="Submit", command=on_market_selected).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_market_selection_gui()