
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from config import *

app = Flask(__name__)

# Database setup (same as before)
DATABASE = '/Users/alcedocoenen/Documents/Plus-Minus/Python/MetaPlus/MetaPlus/MVP01/2. SETUP/2.0 GUI/Config_database/configDB'

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
        conn.execute('UPDATE main.Realisation SET name = ?, author = ?, version = ?, number_of_layers = ? WHERE id = ?',
                     (name, author, version, number_of_layers, id))
    conn.commit()
    conn.close()
    return redirect(url_for('realisations'))


@app.route('/configuration/<int:realisation_number>', methods=['GET', 'POST'])
def configuration(realisation_number):
    realisation = realisation_db.get_by_id(realisation_number)
    if realisation is None:
        return "Realisation not found", 404
    configurations = config_db.get_by_realisation_number(realisation_number)
    selected_config = None
    if request.args.get('layer_id'):
        try:
            selected_layer_id = int(request.args.get('layer_id'))
            selected_config = config_db.get_by_id(selected_layer_id)
        except ValueError:
            pass

    if request.method == 'POST':
        if 'save_config' in request.form:
            layer_id = int(request.form['layer_id'])
            data = {
                "name": request.form['name'],
                "squarepages": request.form['squarepages'],
                "notepages": request.form['notepages'],
                "sequence_offset_start": int(request.form['sequence_offset_start']),
                "sequence_offset_mid": int(request.form['sequence_offset_mid']),
                "sequence_offset_end": int(request.form['sequence_offset_end']),
                "staccato_duration": int(request.form['staccato_duration']),
                "gracenote_offset": int(request.form['gracenote_offset']),
                "cs_instrument": request.form['cs_instrument'],
                "cs_midi_channel": int(request.form['cs_midi_channel']),
                "cs_midi_instrument": int(request.form['cs_midi_instrument']),
                "cs_def_volume": int(request.form['cs_def_volume']),
                "cs_def_duration": int(request.form['cs_def_duration']),
                "acc_instrument": request.form['acc_instrument'],
                "acc_midi_channel": int(request.form['acc_midi_channel']),
                "acc_midi_instrument": int(request.form['acc_midi_instrument']),
                "acc_def_volume": int(request.form['acc_def_volume']),
                "acc_def_duration": int(request.form['acc_def_duration']),
                "acc_pitch_short": int(request.form['acc_pitch_short']),
                "acc_pitch_medium": int(request.form['acc_pitch_medium']),
                "acc_pitch_long": int(request.form['acc_pitch_long']),
                "subs_instrument": request.form['subs_instrument'],
                "subs_midi_channel": int(request.form['subs_midi_channel']),
                "subs_midi_instrument": int(request.form['subs_midi_instrument']),
                "subs_def_volume": int(request.form['subs_def_volume']),
                "subs_def_duration": int(request.form['subs_def_duration']),
                "subs_timepoint_distance": int(request.form['subs_timepoint_distance'])
            }
            if layer_id == 0:
                data['realisation_number'] = realisation_number
                config_db.insert(data)
            else:
                config_db.update(layer_id, data)
            return redirect(url_for('configuration', realisation_number=realisation_number))
        elif 'new_config' in request.form:
            selected_config = {'layer_id': 0, 'name': '', 'squarepages': '', 'notepages': '',
                               'sequence_offset_start': 0, 'sequence_offset_mid': 0, 'sequence_offset_end': 0,
                               'staccato_duration': 0, 'gracenote_offset': 0, 'cs_instrument': '', 'cs_midi_channel': 0,
                               'cs_midi_instrument': 0, 'cs_def_volume': 0, 'cs_def_duration': 0, 'acc_instrument': '',
                               'acc_midi_channel': 0, 'acc_midi_instrument': 0, 'acc_def_volume': 0,
                               'acc_def_duration': 0, 'acc_pitch_short': 0, 'acc_pitch_medium': 0, 'acc_pitch_long': 0,
                               'subs_instrument': '', 'subs_midi_channel': 0, 'subs_midi_instrument': 0,
                               'subs_def_volume': 0, 'subs_def_duration': 0, 'subs_timepoint_distance': 0}

    return render_template('configuration.html', realisation=realisation, configurations=configurations,
                           selected_config=selected_config)


'''
@app.route('/configuration/<int:realisation_number>', methods=['GET', 'POST'])
def configuration(realisation_number):
    conn = get_db_connection()
    realisation = conn.execute('SELECT * FROM main.Realisation WHERE id = ?', (realisation_number,)).fetchone()
    if realisation is None:
        return "Realisation not found", 404
    configurations = conn.execute('SELECT * FROM main.Config_Layer WHERE ref_to_realisation = ?', (realisation_number,)).fetchall()

    selected_configuration = None
    if request.args.get('layer_id'):
        try:
            selected_number = int(request.args.get('layer_id'))
            selected_configuration = conn.execute('SELECT * FROM main.Config_Layer WHERE layer_id = ?', (selected_number,)).fetchone()
        except ValueError:
            pass # Handle invalid input
    conn.close()

    if request.method == 'POST':
        layer_id = request.form['layer_id']
        data = {
            "name": request.form['name'],
            "squarepages": request.form['squarepages'],
            "notepages": request.form['notepages'],
            "sequence_offset_start": int(request.form['sequence_offset_start']),
            "sequence_offset_mid": int(request.form['sequence_offset_mid']),
            "sequence_offset_end": int(request.form['sequence_offset_end']),
            "staccato_duration": int(request.form['staccato_duration']),
            "gracenote_offset": int(request.form['gracenote_offset']),
            "cs_instrument": request.form['cs_instrument'],
            "cs_midi_channel": int(request.form['cs_midi_channel']),
            "cs_midi_instrument": int(request.form['cs_midi_instrument']),
            "cs_def_volume": int(request.form['cs_def_volume']),
            "cs_def_duration": int(request.form['cs_def_duration']),
            "acc_instrument": request.form['acc_instrument'],
            "acc_midi_channel": int(request.form['acc_midi_channel']),
            "acc_midi_instrument": int(request.form['acc_midi_instrument']),
            "acc_def_volume": int(request.form['acc_def_volume']),
            "acc_def_duration": int(request.form['acc_def_duration']),
            "acc_pitch_short": int(request.form['acc_pitch_short']),
            "acc_pitch_medium": int(request.form['acc_pitch_medium']),
            "acc_pitch_long": int(request.form['acc_pitch_long']),
            "subs_instrument": request.form['subs_instrument'],
            "subs_midi_channel": int(request.form['subs_midi_channel']),
            "subs_midi_instrument": int(request.form['subs_midi_instrument']),
            "subs_def_volume": int(request.form['subs_def_volume']),
            "subs_def_duration": int(request.form['subs_def_duration']),
            "subs_timepoint_distance": int(request.form['subs_timepoint_distance'])
        }
        if layer_id == 0:
            data['realisation_number'] = realisation_number
            config_db.insert(data)
        else:
            config_db.update(layer_id, data)
        return redirect(url_for('configuration', realisation_number=realisation_number))

        elif 'new_config' in request.form:
        selected_config = {'layer_id': 0, 'name': '', 'squarepages': '', 'notepages': '', 'sequence_offset_start': 0,
                           'sequence_offset_mid': 0, 'sequence_offset_end': 0, 'staccato_duration': 0, 'gracenote_offset': 0,
                           'cs_instrument': '', 'cs_midi_channel': 0, 'cs_midi_instrument': 0, 'cs_def_volume': 0,
                           'cs_def_duration': 0, 'acc_instrument': '', 'acc_midi_channel': 0, 'acc_midi_instrument': 0,
                           'acc_def_volume': 0, 'acc_def_duration': 0, 'acc_pitch_short': 0, 'acc_pitch_medium': 0,
                           'acc_pitch_long': 0, 'subs_instrument': '', 'subs_midi_channel': 0, 'subs_midi_instrument': 0,
                           'subs_def_volume': 0, 'subs_def_duration': 0, 'subs_timepoint_distance': 0}

        return render_template('configuration.html', realisation=realisation, configurations=configurations,
                               selected_config=selected_config)

columns = ['ref_to_realisation', 'layer_id', 'name', 'squarepages', 'notepages', 'sequence_offset_start',
                   'sequence_offset_mid', 'sequence_offset_end', 'staccato_duration', 'gracenote_offset',
                   'cs_instrument', 'cs_midi_channel', 'cs_midi_instrument', 'cs_def_volume', 'cs_def_duration',
                   'acc_instrument', 'acc_midi_channel', 'acc_midi_instrument', 'acc_def_volume', 'acc_def_duration',
                   'acc_pitch_short', 'acc_pitch_medium', 'acc_pitch_long', 'subs_instrument', 'subs_midi_channel',
                   'subs_midi_instrument', 'subs_def_volume', 'subs_def_duration', 'subs_timepoint_distance']
        columns = ', '.join(columns)
        placeholders = ', '.join(['?'] * 29)
        params = (realisation_number, layer_id, name, squarepages, notepages, sequence_offset_start,
                  sequence_offset_mid, sequence_offset_end, staccato_duration, gracenote_offset,
                  cs_instrument, cs_midi_channel, cs_midi_instrument, cs_def_volume, cs_def_duration,
                  acc_instrument, acc_midi_channel, acc_midi_instrument, acc_def_volume, acc_def_duration,
                  acc_pitch_short, acc_pitch_medium, acc_pitch_long, subs_instrument, subs_midi_channel,
                  subs_midi_instrument, subs_def_volume, subs_def_duration, subs_timepoint_distance)
        sql = f"INSERT INTO main.Config_Layer ({columns}) VALUES ({placeholders})"
        conn.execute(sql, params)
        conn.commit()

        return redirect(url_for('configuration', realisation_number=realisation_number))
    conn.close()
    return render_template('configuration.html', realisation=realisation, configurations=configurations)
'''

if __name__ == '__main__':
    app.run(debug=True)