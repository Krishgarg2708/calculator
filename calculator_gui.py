import tkinter as tk
from tkinter import *
from math import *
import time

# === WINDOW SETUP ===
root = Tk()
root.title("💡 Smart Calculator Pro")
root.geometry("420x600")
root.config(bg="#0f172a")  # Dark blue background
root.resizable(False, False)

# === GLOBAL VARIABLES ===
equation = StringVar()
equation.set("")

# === ENTRY FIELD ===
entry = Entry(root, textvariable=equation, font=("Consolas", 28), bg="#1e293b", fg="#38bdf8",
              bd=0, relief=FLAT, justify="right", insertbackground="#38bdf8")
entry.pack(fill=BOTH, ipadx=8, ipady=15, padx=20, pady=30)

# === HOVER EFFECTS ===
def on_enter(e):
    e.widget['bg'] = "#38bdf8"
    e.widget['fg'] = "#0f172a"

def on_leave(e):
    e.widget['bg'] = "#1e293b"
    e.widget['fg'] = "white"

# === BUTTON CLICK ===
def press(num):
    equation.set(equation.get() + str(num))

def clear():
    equation.set("")

def backspace():
    current = equation.get()
    equation.set(current[:-1])

def equalpress():
    try:
        result = str(eval(equation.get()))
        equation.set(result)
    except:
        equation.set("Error")

# === BUTTON CREATION FUNCTION ===
def create_button(frame, text, cmd=None, color="#1e293b"):
    btn = Button(frame, text=text, font=("Consolas", 20, "bold"), bg=color, fg="white",
                 bd=0, relief=FLAT, activebackground="#38bdf8",
                 activeforeground="#0f172a", command=cmd or (lambda t=text: press(t)))
    btn.pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

# === BUTTON LAYOUT ===
button_frame = Frame(root, bg="#0f172a")
button_frame.pack(expand=True, fill=BOTH)

rows = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for r in rows:
    frame = Frame(button_frame, bg="#0f172a")
    frame.pack(expand=True, fill=BOTH)
    for btn_text in r:
        if btn_text == "=":
            create_button(frame, btn_text, equalpress, "#38bdf8")
        else:
            create_button(frame, btn_text)

# === SPECIAL BUTTONS ===
special_frame = Frame(root, bg="#0f172a")
special_frame.pack(fill=BOTH, padx=10, pady=5)

create_button(special_frame, "C", clear, "#f87171")  # Red for clear
create_button(special_frame, "⌫", backspace, "#fbbf24")  # Yellow for backspace

# === KEYBOARD SUPPORT ===
def key_event(event):
    key = event.char
    if key in '0123456789.+-*/':
        press(key)
    elif key == '\r':  # Enter key
        equalpress()
    elif key == '\x08':  # Backspace
        backspace()

root.bind("<Key>", key_event)

# === TITLE ANIMATION ===
def animate_title():
    while True:
        for color in ["#38bdf8", "#fbbf24", "#34d399", "#f87171", "#c084fc"]:
            root.config(bg=color)
            time.sleep(0.15)
            root.update()
        root.config(bg="#0f172a")

import threading
threading.Thread(target=animate_title, daemon=True).start()

# === START APP ===
root.mainloop()
