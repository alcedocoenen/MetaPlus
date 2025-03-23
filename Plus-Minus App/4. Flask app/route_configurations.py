from flask import Flask, render_template, request, redirect, url_for
from __main__ import app
from database_init import *


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
