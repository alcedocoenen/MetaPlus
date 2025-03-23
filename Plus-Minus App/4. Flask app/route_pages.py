from flask import Flask, render_template, request, redirect, url_for
from __main__ import app
from database_init import *


@app.route('/pages/<int:realisation_number>/<int:layer_id>', methods=['GET','POST'])
def pages(realisation_number, layer_id):
    conn = get_db_connection()
    realisation = realisation_db.get_by_id(realisation_number)
    if realisation is None:
        return "Realisation not found", 404
    configuration = config_db.get_by_real_and_layer(realisation_number, layer_id)
    if configuration is None:
        return "Configuration not found", 404

    conn.close()
    return render_template('pages.html', realisation=realisation, configuration=configuration)
