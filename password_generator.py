import tkinter as tk
from tkinter import messagebox
import random
import string

# Parol yaratish
def generate_password():
    try:
        length = int(length_entry.get())

        chars = ""

        if upper_var.get():
            chars += string.ascii_uppercase

        if lower_var.get():
            chars += string.ascii_lowercase

        if number_var.get():
            chars += string.digits

        if symbol_var.get():
            chars += string.punctuation

        if not chars:
            messagebox.showwarning(
                "Xatolik",
                "Kamida bitta variantni tanlang!"
            )
            return

        password = ''.join(
            random.choice(chars)
            for _ in range(length)
        )

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        strength = check_strength(password)
        strength_label.config(
            text=f"Parol kuchi: {strength}"
        )

    except ValueError:
        messagebox.showerror(
            "Xatolik",
            "Faqat son kiriting!"
        )

# Kuchini tekshirish
def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "🔴 Weak"
    elif score <= 4:
        return "🟡 Medium"
    else:
        return "🟢 Strong"

# Nusxalash
def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo(
            "Tayyor",
            "Parol nusxalandi!"
        )

# Oyna
root = tk.Tk()
root.title("Password Generator Pro")
root.geometry("500x450")
root.resizable(False, False)

# Sarlavha
title = tk.Label(
    root,
    text="🔐 Password Generator Pro",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

# Uzunlik
tk.Label(
    root,
    text="Parol uzunligi:"
).pack()

length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack(pady=5)

# Checkboxlar
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text="Katta harflar (A-Z)",
    variable=upper_var
).pack()

tk.Checkbutton(
    root,
    text="Kichik harflar (a-z)",
    variable=lower_var
).pack()

tk.Checkbutton(
    root,
    text="Raqamlar (0-9)",
    variable=number_var
).pack()

tk.Checkbutton(
    root,
    text="Belgilar (!@#$%)",
    variable=symbol_var
).pack()

# Generate
generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    width=20
)
generate_btn.pack(pady=15)

# Natija
password_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)
password_entry.pack(pady=10)

# Copy
copy_btn = tk.Button(
    root,
    text="📋 Copy Password",
    command=copy_password,
    width=20
)
copy_btn.pack(pady=10)

# Kuch
strength_label = tk.Label(
    root,
    text="Parol kuchi: -",
    font=("Arial", 12)
)
strength_label.pack(pady=10)

root.mainloop()
def save_password():
    password = password_entry.get()

    if password:
        with open("passwords.txt", "a") as file:
            file.write(password + "\n")

        messagebox.showinfo(
            "Saved",
            "Password saqlandi!"
        )
def clear_password():
    password_entry.delete(0, tk.END)
    strength_label.config(text="Parol kuchi: -")
    progress["value"] = 0