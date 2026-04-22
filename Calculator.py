import tkinter as tk

# 1. The Logic: What happens when you click "="
def calculate():
    result = eval(entry.get()) # eval solves the math inside the text box
    entry.delete(0, tk.END)    # clear the box
    entry.insert(tk.END, str(result)) # show the answer

root = tk.Tk()
root.title("Simple Calc")

# 2. The Display Box
entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=3)

# 3. The Buttons (Manual placement is easier to read)
tk.Button(root, text="1", command=lambda: entry.insert(tk.END, "1")).grid(row=1, column=0)
tk.Button(root, text="2", command=lambda: entry.insert(tk.END, "2")).grid(row=1, column=1)
tk.Button(root, text="+", command=lambda: entry.insert(tk.END, "+")).grid(row=1, column=2)

# 4. The Equals Button
tk.Button(root, text="=", command=calculate).grid(row=2, column=0, columnspan=3)

root.mainloop()