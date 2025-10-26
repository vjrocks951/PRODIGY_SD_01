# -------------------------------------------------
# 🌡️ Temperature Converter - GUI Version
# Author: Vijay Kumar
# Description: Converts temperatures between Celsius, Fahrenheit, and Kelvin
# using a Tkinter graphical user interface.
# -------------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        value = float(temp_value.get())
        unit = selected_unit.get()

        if unit == "Celsius (°C)":
            fahrenheit = (value * 9/5) + 32
            kelvin = value + 273.15
            result_label.config(
                text=f"{value}°C = {fahrenheit:.2f}°F\n{value}°C = {kelvin:.2f}K"
            )

        elif unit == "Fahrenheit (°F)":
            celsius = (value - 32) * 5/9
            kelvin = celsius + 273.15
            result_label.config(
                text=f"{value}°F = {celsius:.2f}°C\n{value}°F = {kelvin:.2f}K"
            )

        elif unit == "Kelvin (K)":
            celsius = value - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result_label.config(
                text=f"{value}K = {celsius:.2f}°C\n{value}K = {fahrenheit:.2f}°F"
            )
        else:
            messagebox.showerror("Invalid Unit", "Please select a valid unit.")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for temperature.")

# ---------------------------------------------
# GUI Setup
# ---------------------------------------------
root = tk.Tk()
root.title("🌡️ Temperature Converter")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="#2B2A4C")

title_label = tk.Label(
    root,
    text="Temperature Conversion Program",
    font=("Arial", 16, "bold"),
    bg="#2B2A4C",
    fg="#E8D5C4"
)
title_label.pack(pady=15)

frame = tk.Frame(root, bg="#2B2A4C")
frame.pack(pady=10)

tk.Label(frame, text="Enter Temperature:", font=("Arial", 12), bg="#2B2A4C", fg="white").grid(row=0, column=0, padx=10)
temp_value = tk.Entry(frame, width=10, font=("Arial", 12))
temp_value.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Select Unit:", font=("Arial", 12), bg="#2B2A4C", fg="white").grid(row=1, column=0, padx=10, pady=10)
selected_unit = ttk.Combobox(frame, values=["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"], state="readonly", font=("Arial", 11))
selected_unit.grid(row=1, column=1, padx=5)
selected_unit.current(0)

convert_btn = tk.Button(
    root,
    text="Convert",
    command=convert_temperature,
    font=("Arial", 13, "bold"),
    bg="#EA906C",
    fg="white",
    relief="raised",
    padx=20,
    pady=5
)
convert_btn.pack(pady=15)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 13, "bold"),
    bg="#2B2A4C",
    fg="#EEE2DE",
    justify="center"
)
result_label.pack(pady=10)

footer_label = tk.Label(
    root,
    text="Developed by Your Name",
    font=("Arial", 9),
    bg="#2B2A4C",
    fg="#B2B2B2"
)
footer_label.pack(side="bottom", pady=10)

root.mainloop()
