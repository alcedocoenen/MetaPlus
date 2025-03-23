from flask import Flask, render_template, request, redirect, url_for
from __main__ import app
from database_init import *
import PlusMinusSquarePageAdditions


@app.route('/page_detail/<int:symbolpagenr>/<int:notepagenr>', methods=['GET', 'POST'])
def page_detail(symbolpagenr, notepagenr):
    # TODO get pts[x] from PlusMinusSquarePageAdditions.py
    pts = PlusMinusSquarePageAdditions.page_tendency_statements[symbolpagenr-1]
    # make the pts displayable info for the page
    return render_template('page_detail.html', symbolpagenr=symbolpagenr, notepagenr=notepagenr, pts=pts)
