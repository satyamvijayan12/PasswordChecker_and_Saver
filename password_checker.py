import tkinter as tk
from tkinter import messagebox
import hashlib
import re

def check_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r'[A-Z]', password): score += 1
    if re.search(r'[a-z]', password): score += 1
    if re.search(r'[0-9]', password): score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): score += 1
    return score

def evaluate():
    pwd = entry.get()
    strength = check_strength(pwd)
    labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong", "Excellent"]
    label_result.config(text=f"Strength: {labels[strength]}")

def store_password():
    pwd = entry.get()
    if pwd:
        hashed = hashlib.sha256(pwd.encode()).hexdigest()
        with open("passwords.txt", "a") as f:
            f.write(f"{hashed}\n")
        messagebox.showinfo("Saved", "Password hashed and stored safely.")
    else:
        messagebox.showwarning("Empty", "Enter a password before saving.")

# UI Setup
app = tk.Tk()
app.title("Password Strength Checker")
app.geometry("350x200")

tk.Label(app, text="Enter your password:").pack(pady=5)
entry = tk.Entry(app, width=30, show="*")
entry.pack()

tk.Button(app, text="Check Strength", command=evaluate).pack(pady=5)
label_result = tk.Label(app, text="Strength: ")
label_result.pack(pady=5)

tk.Button(app, text="Save (SHA-256)", command=store_password).pack(pady=10)

app.mainloop()