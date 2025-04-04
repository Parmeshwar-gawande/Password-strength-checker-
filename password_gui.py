import tkinter as tk
import re

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'\d', password):
        strength += 1
    if re.search(r'[^A-Za-z0-9]', password):
        strength += 1

    return strength

def update_strength_meter():
    password = password_entry.get()
    strength = check_password_strength(password)

    if strength == 5:
        strength_label.config(text="🔥 Very Strong", fg="green")
    elif strength == 4:
        strength_label.config(text="💪 Strong", fg="yellowgreen")
    elif strength == 3:
        strength_label.config(text="🟡 Medium", fg="orange")
    elif strength == 2:
        strength_label.config(text="🟠 Weak", fg="red")
    else:
        strength_label.config(text="🔴 Very Weak", fg="darkred")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

tk.Label(root, text="Enter Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)
password_entry.bind("<KeyRelease>", lambda event: update_strength_meter())

strength_label = tk.Label(root, text="Strength: ?", font=("Arial", 12))
strength_label.pack(pady=10)

root.mainloop()
