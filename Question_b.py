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


def save_to_db(username, specimen_size, actual_size):
    conn = sqlite3.connect('specimens.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO specimens (username, specimen_size, actual_size)
        VALUES (?, ?, ?)
    ''', (username, specimen_size, actual_size))
    conn.commit()
    conn.close()


init_db()

def calculate_real_size(microscope_size, magnification_factor=100):
    
    return microscope_size / magnification_factor


username = input("Enter your username: ")
microscope_size = float(input("Enter microscope size (in mm): "))
actual_size = calculate_real_size(microscope_size)
save_to_db(username, microscope_size, actual_size)
print(f"Saved: {username} - {microscope_size} mm -> {actual_size:.2f} mm")
