from flask import Flask, render_template, request, redirect, url_for
from __main__ import app
from database_init import *



@app.route('/delete_realisation/<int:realisation_number>', methods=['GET', 'POST'])
def delete_realisation(realisation_number):
    conn = get_db_connection()
    realisation_db.delete(realisation_number)
    conn.commit()
    conn.close()
    return redirect(url_for('realisations'))
