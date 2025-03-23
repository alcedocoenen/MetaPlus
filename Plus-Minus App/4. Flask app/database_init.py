
import sqlite3
import os

from config_PageDB import Config_PageDB
from config_realisationDB import RealisationDB
from config_config import Config
from config_squareDB import Config_SquareDB

# Database setup
DATABASE = '/Users/alcedocoenen/Documents/Plus-Minus/Python/MetaPlus/MetaPlus/Plus-Minus App/2. Config_database/configDB'

realisation_db = RealisationDB(DATABASE)
realisation_db.create_table()
config_db = Config(DATABASE)
config_db.create_table()

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
