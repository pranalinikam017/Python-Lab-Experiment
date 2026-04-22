import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("My App")
root.geometry("300x200")

# Add a text label
label = tk.Label(root, text="Welcome to GUI Programming")
label.pack(pady=20)

# Add a button
button = tk.Button(root, text="Exit", command=root.quit)
button.pack()

# Start the application
root.mainloop()