from flask import Flask, render_template, request, redirect, url_for
from __main__ import app
from database_init import *


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

    squarepages = validated(squarepages)
    notepages = validated(notepages)

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
