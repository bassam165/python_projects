import tkinter as tk
from tkinter import filedialog
import pandas as pd
import openpyxl


def compare_excel_files():
    file1_path = file1_entry.get()
    file2_path = file2_entry.get()

    if not file1_path or not file2_path:
        result_label.config(text="Please select both files.")
        return

    try:
        df1 = pd.read_excel(file1_path)
        df2 = pd.read_excel(file2_path)
    except Exception as e:
        result_label.config(text=f"Error: {e}")
        return

    result_set = set()
    for name in df1.iloc[:, 0]:
        if name in df2.iloc[:, 1].values:
            result_set.add(df2.loc[df2.iloc[:, 1] == name, df2.columns[0]].values[0])

    if result_set:
        result_label.config(text=f"Matching data in File 2: {sorted(result_set)}")
        
        # Save the matching data to a new Excel file
        save_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if save_path:
            result_df = pd.DataFrame(sorted(result_set), columns=["Matched Data"])
            result_df.to_excel(save_path, index=False)
            result_label.config(text=f"Matching data saved to {save_path}")
    else:
        result_label.config(text="No matches found.")

def browse_file1():
    file1_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    file1_entry.delete(0, tk.END)
    file1_entry.insert(0, file1_path)

def browse_file2():
    file2_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    file2_entry.delete(0, tk.END)
    file2_entry.insert(0, file2_path)

# main window
window = tk.Tk()
window.title("Attendy")
window.geometry("600x400")
window.configure(bg="#8dbcaa")
window.iconbitmap("icon.ico")

# widgets
file1_label = tk.Label(window, text="Select Excel File 1:", bg="#d4e6df",padx=20, pady=8, borderwidth=1, relief="sunken")
file1_label.configure(font=("TkDefaultFont", 16)) 
file1_label.pack(padx=10, pady=10)

file1_entry = tk.Entry(window)
file1_entry.pack(padx=5, pady=5)

browse_button1 = tk.Button(window, text="Browse", command=browse_file1, padx=20, pady=8, bg="#e3eeea", borderwidth=1, relief="ridge")
browse_button1.pack(padx=5, pady=5)

file2_label = tk.Label(window, text="Select Excel File 2:", padx=20, pady=8, bg="#d4e6df", borderwidth=1, relief="sunken")
file2_label.configure(font=("TkDefaultFont", 16))
file2_label.pack(padx=5, pady=5)

file2_entry = tk.Entry(window)
file2_entry.pack(padx=5, pady=5)

browse_button2 = tk.Button(window, text="Browse", command=browse_file2, padx=20, pady=8, bg="#e3eeea", borderwidth=1, relief="ridge")
browse_button2.pack(padx=5, pady=5)

compare_button = tk.Button(window, text="Display & Save", command=compare_excel_files, padx=20, pady=8, bg="#e3eeea", borderwidth=1, relief="ridge")
compare_button.pack(padx=5, pady=5)

result_label = tk.Label(window, text="")
result_label.pack(padx=5, pady=5)

bottom_label = tk.Label(window, text="© 2022-2023 Abdullah Al Bassam. All rights reserved.", bg="#8dbcaa")
bottom_label.pack(side=tk.BOTTOM, fill=tk.X)

window.mainloop()
