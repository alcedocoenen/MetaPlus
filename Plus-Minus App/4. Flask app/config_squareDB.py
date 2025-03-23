import sqlite3

class Config_SquareDB:  # class for config_layer table
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        self.table_name = "Config_Square"

    def _connect(self):  # same as in ConfigDB
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
            return self.conn
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return None

    def _close(self):  # same as in ConfigDB
        if self.conn:
            self.conn.close()
            self.conn = None

    def create_table(self):
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS {self.table_name} (
                        square_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        square_nr INTEGER,
                        preferred_changedir INTEGER,
                        replaced_changevalue INTEGER,
                        ref_to_page INTEGER
                    )
                """)
                conn.commit()
                print(f"Table '{self.table_name}' created (or already exists).")
            except sqlite3.Error as e:
                print(f"Error creating table: {e}")
            finally:
                self._close()

    def get_all(self):
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {self.table_name}")
                return cursor.fetchall()
            except sqlite3.Error as e:
                print(f"Error getting data: {e}")
                return None
            finally:
                self._close()

    def get_by_id(self, number):
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {self.table_name} WHERE square_id = ?", (number,))
                return cursor.fetchone()
            except sqlite3.Error as e:
                print(f"Error getting data: {e}")
                return None
            finally:
                self._close()

    def get_by_page_id(self, page_id):
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {self.table_name} WHERE ref_to_page = ?", (page_id,))
                return cursor.fetchall()
            except sqlite3.Error as e:
                print(f"Error getting data: {e}")
                return None
            finally:
                self._close()

    def insert(self, data):  # similar to ConfigDB
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                placeholders = ", ".join(["?"] * len(data))
                columns = ", ".join(data.keys())
                sql = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
                cursor.execute(sql, list(data.values()))
                conn.commit()
                return cursor.lastrowid
            except sqlite3.Error as e:
                print(f"Error inserting data: {e}")
                return None
            finally:
                self._close()

    def update(self, number, data):  # similar to ConfigDB
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                updates = ", ".join([f"{key} = ?" for key in data.keys()])
                sql = f"UPDATE {self.table_name} SET {updates} WHERE square_id = ?"
                values = list(data.values())
                values.append(number)
                cursor.execute(sql, values)
                conn.commit()
                return cursor.rowcount
            except sqlite3.Error as e:
                print(f"Error updating data: {e}")
                return None
            finally:
                self._close()

    def delete(self, number):
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                sql = f"DELETE FROM {self.table_name} WHERE square_id = ?"

                cursor.execute(sql, (number,))
                conn.commit()
                return cursor.rowcount
            except sqlite3.Error as e:
                print(f"Error deleting data: {e}")
                return None

            finally:
                self._close()
