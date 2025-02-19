
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
    #realisations_data = conn.execute('SELECT * FROM main.Realisation').fetchall()
    realisations_data = realisation_db.get_all()
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
    data = {"name": name, "author": author, "version": version, "number_of_layers": number_of_layers}

    if id == 0:
         realisation_db.insert(data)
    else:
        realisation_db.update(id,data)
    conn.commit()
    conn.close()
    return redirect(url_for('realisations'))

@app.route('/delete_realisation/<int:realisation_number>', methods=['GET', 'POST'])
def delete_realisation(realisation_number):
    conn = get_db_connection()
    realisation_db.delete(realisation_number)
    conn.commit()
    conn.close()
    return redirect(url_for('realisations'))

@app.route('/configurations/<int:realisation_number>', methods=['GET', 'POST'])
def configuration(realisation_number):
    conn = get_db_connection()
    realisation = realisation_db.get_by_id(realisation_number)
    if realisation is None:
        return "Realisation not found", 404
    configuration_data = config_db.get_by_realisation_number(realisation_number)
    selected_config = None
    if request.args.get('layer_id'):
        try:
            selected_layer_id = int(request.args.get('layer_id'))
            selected_config = config_db.get_by_id(selected_layer_id)
        except ValueError:
            return "Invalid layer ID", 400
            pass

    conn.close()
    # print (configuration_data)
    return render_template('configurations.html', realisation=realisation, configurations=configuration_data,
                           selected_config=selected_config)

@app.route('/save_configuration/<int:realisation_number>', methods=['POST']) #New route for saving
def save_configuration(realisation_number):
    conn = get_db_connection()
    ref_to_realisation = realisation_number
    layer_id = int(request.form['layer_id'])
    name = request.form['name']
    squarepages = request.form['squarepages']
    notepages = request.form['notepages']
    sequence_offset_start = request.form['sequence_offset_start']
    sequence_offset_mid = request.form['sequence_offset_mid']
    sequence_offset_end = request.form['sequence_offset_end']
    staccato_duration = request.form['staccato_duration']
    gracenote_offset = request.form['gracenote_offset']
    cs_instrument = request.form['cs_instrument']
    cs_midi_channel = request.form['cs_midi_channel']
    cs_midi_instrument = request.form['cs_midi_instrument']
    cs_def_volume = request.form['cs_def_volume']
    cs_def_duration = request.form['cs_def_duration']
    acc_instrument = request.form['acc_instrument']
    acc_midi_instrument = request.form['acc_midi_instrument']
    acc_midi_channel = request.form['acc_midi_channel']
    acc_def_volume = request.form['acc_def_volume']
    acc_def_duration = request.form['acc_def_duration']
    acc_pitch_short = request.form['acc_pitch_short']
    acc_pitch_medium = request.form['acc_pitch_medium']
    acc_pitch_long = request.form['acc_pitch_long']
    subs_instrument = request.form['subs_instrument']
    subs_midi_instrument = request.form['subs_midi_instrument']
    subs_midi_channel = request.form['subs_midi_channel']
    subs_def_volume = request.form['subs_def_volume']
    subs_def_duration = request.form['subs_def_duration']
    subs_timepoint_distance = request.form['subs_timepoint_distance']



    #TODO ook moet worden afgevangen dat er niet meer dan 7 lagen mogen zijn.
    data = {'name': name, 'squarepages': squarepages, 'notepages': notepages,
            'ref_to_realisation': ref_to_realisation, 'sequence_offset_start': sequence_offset_start,
            'sequence_offset_mid': sequence_offset_mid, 'sequence_offset_end': sequence_offset_end,
            'staccato_duration': staccato_duration, 'gracenote_offset': gracenote_offset,
            'cs_instrument': cs_instrument, 'cs_midi_channel': cs_midi_channel,
            'cs_midi_instrument': cs_midi_instrument, 'cs_def_volume': cs_def_volume,
            'cs_def_duration': cs_def_duration, 'acc_instrument': acc_instrument,
            'acc_midi_instrument': acc_midi_instrument, 'acc_midi_channel': acc_midi_channel,
            'acc_def_volume': acc_def_volume, 'acc_def_duration': acc_def_duration, 'acc_pitch_short': acc_pitch_short,
            'acc_pitch_medium': acc_pitch_medium, 'acc_pitch_long': acc_pitch_long, 'subs_instrument': subs_instrument,
            'subs_midi_instrument': subs_midi_instrument, 'subs_midi_channel': subs_midi_channel,
            'subs_def_volume': subs_def_volume, 'subs_def_duration': subs_def_duration,
            'subs_timepoint_distance': subs_timepoint_distance}

    if layer_id == 0:

        config_db.insert(data)
        #conn.execute('INSERT INTO main.Realisation (name, author, version, number_of_layers) VALUES (?, ?, ?, ?)',
         #            (name, author, version, number_of_layers))
    else:
        config_db.update(layer_id,data)
        #conn.execute('UPDATE main.Realisation SET name = ?, author = ?, version = ?, number_of_layers = ? WHERE id = ?',
         #            (name, author, version, number_of_layers, id))
    conn.commit()
    conn.close()
    return redirect(url_for('configuration',realisation_number=realisation_number))

@app.route('/delete_configuration/<int:realisation_number>/<int:layer_id>', methods=['GET', 'POST'])
def delete_configuration(realisation_number, layer_id):
    conn = get_db_connection()
    config_db.delete(layer_id)
    conn.commit()
    conn.close()
    return redirect(url_for('configuration',realisation_number=realisation_number))


if __name__ == '__main__':
    app.run(debug=True)