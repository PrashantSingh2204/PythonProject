import tkinter as tk

def click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=3, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+",
    "C"
]

row, col = 1, 0
for btn in buttons:
    action = lambda x=btn: click(x)
    tk.Button(root, text=btn, width=5, height=2, font=("Arial", 14), command=action)\
        .grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()