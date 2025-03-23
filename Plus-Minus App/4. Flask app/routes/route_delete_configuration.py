from flask import Flask, render_template, request, redirect, url_for
from __main__ import app
from database_init import *


@app.route('/delete_configuration/<int:realisation_number>/<int:layer_id>', methods=['GET', 'POST'])
def delete_configuration(realisation_number, layer_id):
    conn = get_db_connection()
    config_db.delete(layer_id)
    conn.commit()
    conn.close()
    return redirect(url_for('configuration',realisation_number=realisation_number))
