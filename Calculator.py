import tkinter as tk

def click(val):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(val))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# -------- WINDOW --------
root = tk.Tk()
root.title("Calculator Pro")
root.geometry("500x600")
root.configure(bg="#0f172a")

# CENTER CARD
card = tk.Frame(root, bg="#1e293b")
card.place(relx=0.5, rely=0.5, anchor="center", width=280, height=420)

# DISPLAY
entry = tk.Entry(card,
                 font=("Segoe UI", 22, "bold"),
                 bd=0,
                 justify="right",
                 bg="#1e293b",
                 fg="#ffffff",
                 insertbackground="white")
entry.pack(fill="both", padx=10, pady=15, ipady=10)

# BUTTON STYLE FUNCTION
def create_btn(parent, text, color, cmd):
    return tk.Button(parent,
                     text=text,
                     font=("Segoe UI", 13, "bold"),
                     bg=color,
                     fg="white",
                     bd=0,
                     activebackground="#6366f1",
                     command=cmd)

# BUTTONS
buttons = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','=','+')
]

for row in buttons:
    row_frame = tk.Frame(card, bg="#1e293b")
    row_frame.pack(expand=True, fill="both", padx=8, pady=3)

    for btn in row:
        if btn == "=":
            action = calculate
            color = "#6366f1"   # highlight
        elif btn in "+-*/":
            action = lambda x=btn: click(x)
            color = "#475569"   # operator color
        else:
            action = lambda x=btn: click(x)
            color = "#334155"

        create_btn(row_frame, btn, color, action)\
            .pack(side="left", expand=True, fill="both", padx=3, pady=3)

# CLEAR BUTTON
create_btn(card, "AC", "#ef4444", clear)\
    .pack(fill="both", padx=10, pady=10)

root.mainloop()
