from flask import Flask, render_template, request, redirect, url_for
from __main__ import app
from database_init import *

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

