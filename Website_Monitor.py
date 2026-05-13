import tkinter as tk
from tkinter import ttk
import requests
import time

# Store websites
websites = []

def add_website():
    url = entry.get().strip()
    if url:
        if not url.startswith("http"):
            url = "https://" + url
        websites.append(url)
        listbox.insert(tk.END, url)
        entry.delete(0, tk.END)

def check_all():
    for row in tree.get_children():
        tree.delete(row)

    for site in websites:
        try:
            start = time.time()
            response = requests.get(site, timeout=5)
            end = time.time()

            time_taken = round(end - start, 3)

            if response.status_code == 200:
                status = "UP"
            else:
                status = "DOWN"

        except:
            status = "ERROR"
            time_taken = "-"

        tree.insert("", tk.END, values=(site, status, time_taken))

# -------- UI --------
root = tk.Tk()
root.title("Website Monitor Pro++")
root.geometry("600x400")
root.configure(bg="#1e1e2f")

# Title
tk.Label(root, text="🌐 Website Monitor Pro++",
         font=("Segoe UI", 16, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=10)

# Input
entry = tk.Entry(root, font=("Segoe UI", 11), width=30)
entry.pack(pady=5)

tk.Button(root, text="Add Website", command=add_website).pack(pady=5)
tk.Button(root, text="Check All", command=check_all).pack(pady=5)

# List
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Table
columns = ("Website", "Status", "Time (s)")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(fill="both", expand=True)

root.mainloop()
