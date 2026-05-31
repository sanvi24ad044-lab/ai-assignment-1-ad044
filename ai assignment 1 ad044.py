import tkinter as tk
from tkinter import messagebox

# Information database
info = {
    "python": "Python is a high-level programming language used for web development, AI, data science, and automation.",
    "java": "Java is an object-oriented programming language used for developing desktop, web, and mobile applications.",
    "ai": "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",
    "dbms": "DBMS stands for Database Management System. It is used to store, manage, and retrieve data efficiently.",
    "computer": "A computer is an electronic device that processes data and produces meaningful information."
}

def search():
    topic = entry.get().strip().lower()

    if topic == "":
        messagebox.showwarning("Warning", "Please enter a topic!")
        return

    if topic in info:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, info[topic])
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"No information found for '{topic}'.")

# Main Window
root = tk.Tk()
root.title("Information Bot")
root.geometry("600x400")

# Heading
title = tk.Label(root, text="Information Bot", font=("Arial", 18, "bold"))
title.pack(pady=10)

# Search Box
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

# Search Button
search_btn = tk.Button(root, text="Search", command=search)
search_btn.pack(pady=5)

# Result Area
result_text = tk.Text(root, height=10, width=60, font=("Arial", 11))
result_text.pack(pady=10)

root.mainloop()
