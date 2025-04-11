from tkinter import Tk, Label, Entry, Button
import sqlite3

def init_db():
    conn = sqlite3.connect('specimens.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS specimens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            specimen_size REAL,
            actual_size REAL
        )
    ''')
    conn.commit()
    conn.close()

def calculate_real_size(microscope_size, magnification_factor=100):
    
    return microscope_size / magnification_factor


def save_to_db(username, specimen_size, actual_size):
    conn = sqlite3.connect('specimens.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO specimens (username, specimen_size, actual_size)
        VALUES (?, ?, ?)
    ''', (username, specimen_size, actual_size))
    conn.commit()
    conn.close()

def run_tkinter_gui():
    def on_submit():
        username = username_entry.get()
        try:
            specimen_size = float(size_entry.get())
            actual_size = calculate_real_size(specimen_size)
            save_to_db(username, specimen_size, actual_size)
            result_label.config(text=f"Actual Size: {actual_size:.2f} mm")
        except ValueError:
            result_label.config(text="Please enter a valid number!")



    window = Tk()
    window.title("Microscope Size Calculator")

    Label(window, text="Username").pack()
    username_entry = Entry(window)
    username_entry.pack()

    Label(window, text="Microscope Size (mm)").pack()
    size_entry = Entry(window)
    size_entry.pack()

    Button(window, text="Calculate", command=on_submit).pack()
    result_label = Label(window, text="")
    result_label.pack()

    window.mainloop()


run_tkinter_gui()
