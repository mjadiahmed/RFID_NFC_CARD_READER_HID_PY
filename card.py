import keyboard
import tkinter as tk
from tkinter import ttk
import time

kbd_buffer = []
last_input_time = time.time()

def reset_buffer():
    """Clear previous buffer when noise or wrong layout detected."""
    global kbd_buffer
    kbd_buffer.clear()
    dec_var.set("")
    hex_var.set("")

def on_kb_event(e):
    """Handle key presses from an HID keyboard-style RFID reader."""
    global kbd_buffer, last_input_time

    if e.event_type != 'down':
        return

    name = e.name
    current_time = time.time()

    # Reset buffer if there's a long gap or invalid data
    if current_time - last_input_time > 1.0:
        reset_buffer()
    last_input_time = current_time

    if name == 'enter':
        if kbd_buffer:
            s = ''.join(kbd_buffer)
            try:
                dec_value = int(s)
                hex_value = format(dec_value, 'X')

                # Update GUI
                dec_var.set(f"{dec_value:010d}")
                hex_var.set(hex_value.upper())

                print(f"\nDEC: {dec_value:010d}")
                print(f"HEX: {hex_value.upper()}")
                print("-" * 30)

            except ValueError:
                dec_var.set("Invalid Input")
                hex_var.set("Check Layout (ENG)")
            finally:
                kbd_buffer.clear()
    else:
        # Append only digits (ignore letters or accented chars from FR layout)
        if len(name) == 1 and name.isdigit():
            kbd_buffer.append(name)
        elif name.lower().startswith('num '):
            ch = name.split(' ')[1]
            if ch.isdigit():
                kbd_buffer.append(ch)
        else:
            reset_buffer()

# --- GUI setup ---
root = tk.Tk()
root.title("RFID / NFC Reader")
root.geometry("440x280")
root.configure(bg="#f5f5f7")
root.resizable(False, False)

#  aesthetic theme
style = ttk.Style()
style.theme_use("clam")

#  font and soft UI design
style.configure(
    "TLabel",
    font=("SF Pro Display", 11),
    background="#f5f5f7",
    foreground="#1d1d1f"
)
style.configure(
    "Rounded.TFrame",
    background="#ffffff",
    relief="flat"
)
style.configure(
    "TEntry",
    font=("SF Mono", 13),
    fieldbackground="#fbfbfc",
    foreground="#000",
    borderwidth=0,
    padding=8
)
style.map("TEntry", fieldbackground=[("readonly", "#f0f0f3")])

# Add subtle rounded shadow frame
outer = tk.Frame(root, bg="#d1d1d6", bd=0)
outer.pack(padx=18, pady=(25, 20), fill="both", expand=True)

inner = tk.Frame(outer, bg="#ffffff", bd=0, highlightthickness=0)
inner.pack(padx=2, pady=2, fill="both", expand=True)
inner.configure(highlightbackground="#e5e5ea", highlightthickness=1)

title_label = ttk.Label(
    inner,
    text="RFID / NFC Card Reader",
    font=("SF Pro Display", 15, "bold"),
    background="#ffffff",
)
title_label.pack(pady=(20, 5))

subtitle_label = ttk.Label(
    inner,
    text="Switch your keyboard layout to English (US)\nThen scan your card below",
    font=("SF Pro Display", 10),
    foreground="#6e6e73",
    background="#ffffff",
    justify="center",
)
subtitle_label.pack(pady=(0, 10))

# Content frame
frame = ttk.Frame(inner, padding=15, style="Rounded.TFrame")
frame.pack(pady=5)

ttk.Label(frame, text="Decimal (DEC):").grid(row=0, column=0, sticky="w", padx=5, pady=8)
ttk.Label(frame, text="Hexadecimal (HEX):").grid(row=1, column=0, sticky="w", padx=5, pady=8)

dec_var = tk.StringVar()
hex_var = tk.StringVar()

dec_entry = ttk.Entry(frame, textvariable=dec_var, width=28, state="readonly", justify="center")
hex_entry = ttk.Entry(frame, textvariable=hex_var, width=28, state="readonly", justify="center")

dec_entry.grid(row=0, column=1, padx=5, pady=8)
hex_entry.grid(row=1, column=1, padx=5, pady=8)

footer_label = ttk.Label(
    inner,
    text="💡 Tip: If you see 'Invalid Input', switch to ENG layout",
    font=("SF Pro Display", 9),
    foreground="#9c9ca1",
    background="#ffffff"
)
footer_label.pack(side="bottom", pady=10)

# Hook keyboard events
keyboard.hook(on_kb_event)

root.mainloop()
