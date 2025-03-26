from flask import Flask, render_template, request, redirect, url_for
from __main__ import app
from database_init import *
import PlusMinusSquareData as pmsq
import PlusMinusNotepageChords as pmch
import PlusMinusNotepageSubs as pmsu


@app.route('/square_detail/<int:symbolpagenr>/<int:notepagenr>/<int:squarenr>', methods=['GET'])
def square_detail(symbolpagenr, notepagenr, squarenr):
    # get symbolpage
    square = pmsq.symbolpages[symbolpagenr][squarenr]
    type = square[22]
    substype = square[13]
    chords = pmch.allchordnotepages[notepagenr][type-1]
    subsnotes = pmsu.allsubsnotepages[notepagenr][substype-1]
    notes = [type, substype, chords,subsnotes]
    return render_template('square_detail.html',symbolpagenr=symbolpagenr, notepagenr=notepagenr, squarenr=squarenr, square=square, notes=notes)
