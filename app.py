from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<html>
  <head><title>Microscope Size Calculator</title></head>
  <body>
    <h2>Microscope Size Calculator</h2>
    <form method="post">
        Username: <input type="text" name="username"><br><br>
        Microscope Size (mm): <input type="number" name="microscope_size" step="0.01"><br><br>
        <input type="submit" value="Calculate">
    </form>
    {% if result %}
        <h3>Actual Size: {{ result }} mm</h3>
    {% endif %}
  </body>
</html>
'''
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
    
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        username = request.form['username']
        specimen_size = float(request.form['microscope_size'])
        actual_size = calculate_real_size(specimen_size)
        save_to_db(username, specimen_size, actual_size)
        result = f"{actual_size:.2f}"
    return render_template_string(HTML_TEMPLATE, result=result)


app.run(host='0.0.0.0', port=5000)

