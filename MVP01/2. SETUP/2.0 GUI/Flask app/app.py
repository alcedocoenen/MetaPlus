
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Database setup (same as before)
DATABASE = '/Users/alcedocoenen/Documents/Plus-Minus/Python/MetaPlus/MetaPlus/MVP01/2. SETUP/2.0 GUI/Config_database/configDB'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(): # same as before
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Realisation (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                author TEXT,
                version TEXT,
                number_of_layers INTEGER
            )
        """)
        conn.commit()

if not os.path.exists(DATABASE):
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/realisations', methods=['GET', 'POST'])
def realisations():
    conn = get_db_connection()
    realisations_data = conn.execute('SELECT * FROM main.Realisation').fetchall()
    selected_realisation = None
    if request.args.get('id'):
        try:
            selected_number = int(request.args.get('id'))
            selected_realisation = conn.execute('SELECT * FROM main.Realisation WHERE id = ?', (selected_number,)).fetchone()
        except ValueError:
            pass # Handle invalid input
    conn.close()
    return render_template('realisations.html', realisations=realisations_data, selected_realisation=selected_realisation)


@app.route('/save_realisation', methods=['POST']) #New route for saving
def save_realisation():
    conn = get_db_connection()
    id = int(request.form['id'])
    name = request.form['name']
    author = request.form['author']
    version = request.form['version']
    try:
        number_of_layers = int(request.form['number_of_layers'])
    except ValueError:
        number_of_layers = 0

    if id == 0:
        conn.execute('INSERT INTO main.Realisation (name, author, version, number_of_layers) VALUES (?, ?, ?, ?)',
                     (name, author, version, number_of_layers))
    else:
        conn.execute('UPDATE main.Realisation SET name = ?, author = ?, version = ?, number_of_layers = ? WHERE number = ?',
                     (name, author, version, number_of_layers, id))
    conn.commit()
    conn.close()
    return redirect(url_for('realisations'))

if __name__ == '__main__':
    app.run(debug=True)