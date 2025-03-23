from flask import Flask, render_template, request, redirect, url_for
from __main__ import app
from database_init import *


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

