import sqlite3

class Config:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        self.table_name = "Config_Layer"

    def _connect(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row  # Return rows as dictionaries
            return self.conn
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return None

    def _close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def create_table(self):
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS config (
                        layer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        squarepages TEXT,
                        notepages TEXT,
                        sequence_offset_start INTEGER,
                        sequence_offset_mid INTEGER,
                        sequence_offset_end INTEGER,
                        staccato_duration INTEGER,
                        gracenote_offset INTEGER,
                        cs_instrument TEXT,
                        cs_midi_channel INTEGER,
                        cs_midi_instrument INTEGER,
                        cs_def_volume INTEGER,
                        cs_def_duration INTEGER,
                        acc_instrument TEXT,
                        acc_midi_channel INTEGER,
                        acc_midi_instrument INTEGER,
                        acc_def_volume INTEGER,
                        acc_def_duration INTEGER,
                        acc_pitch_short INTEGER,
                        acc_pitch_medium INTEGER,
                        acc_pitch_long INTEGER,
                        subs_instrument TEXT,
                        subs_midi_channel INTEGER,
                        subs_midi_instrument INTEGER,
                        subs_def_volume INTEGER,
                        subs_def_duration INTEGER,
                        subs_timepoint_distance INTEGER
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

    def insert(self, data):
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                placeholders = ", ".join(["?"] * len(data))
                columns = ", ".join(data.keys())
                sql = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
                cursor.execute(sql, list(data.values()))
                conn.commit()
                return cursor.lastrowid  # return the ID of the last inserted row
            except sqlite3.Error as e:
                print(f"Error inserting data: {e}")
                return None
            finally:
                self._close()

    def update(self, layer_id, data):
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                updates = ", ".join([f"{key} = ?" for key in data.keys()])
                sql = f"UPDATE {self.table_name} SET {updates} WHERE layer_id = ?"
                values = list(data.values())
                values.append(layer_id)
                cursor.execute(sql, values)
                conn.commit()
                return cursor.rowcount  # return the number of updated rows
            except sqlite3.Error as e:
                print(f"Error updating data: {e}")
                return None
            finally:
                self._close()


    def delete(self, layer_id):
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                sql = f"DELETE FROM {self.table_name} WHERE layer_id = ?"

                cursor.execute(sql, (layer_id,))
                conn.commit()
                return cursor.rowcount  # return the number of deleted rows
            except sqlite3.Error as e:
                print(f"Error deleting data: {e}")
                return None
            finally:
                self._close()

    def get_by_id(self, layer_id):
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {self.table_name} WHERE layer_id = ?", (layer_id,))
                return cursor.fetchone()
            except sqlite3.Error as e:
                print(f"Error getting data: {e}")
                return None
            finally:
                self._close()

    def get_by_realisation_number(self, realisation_number):
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                #ealisation_string = str(realisation_number)
                #sql_statement = "SELECT * FROM " + self.table_name + " WHERE ref_to_realisation = " + realisation_string
                #cursor.execute(sql_statement)
                cursor.execute(f"SELECT * FROM {self.table_name} WHERE ref_to_realisation = ?", (realisation_number,))
                return cursor.fetchall()
            except sqlite3.Error as e:
                print(f"Error getting data: {e}")
                return None
            finally:
                self._close()

    def get_by_real_and_layer(self, realisation_number, layer_id):
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {self.table_name} WHERE ref_to_realisation = ? AND layer_id = ?", (realisation_number, layer_id))
                return cursor.fetchone()
            except sqlite3.Error as e:
                print(f"Error getting data: {e}")
                return None
            finally:
                self._close()
