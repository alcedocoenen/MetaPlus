from flask import Flask, render_template, request, redirect, url_for
from __main__ import app
from database_init import *


@app.route('/square_detail/<int:realisation_number>/<int:layer_id>/<int:page_id>/<int:squarenr>', methods=['GET', 'POST'])
def square_detail(realisation_number, layer_id, page_id, squarenr):
    return render_template('square_detail.html',realisation=realisation_number, layer=layer_id, page=page_id, square=squarenr)
