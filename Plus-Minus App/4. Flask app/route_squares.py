from flask import Flask, render_template, request, redirect, url_for
from __main__ import app
from database_init import *


@app.route('/squares/<int:realisation_number>/<int:layer_id>/<int:page_id>', methods=['GET', 'POST'])
def squares(realisation_number, layer_id, page_id):
    return render_template('squares.html',realisation=realisation_number, layer=layer_id, page=page_id)
