
from flask import Flask, render_template


app = Flask(__name__)

import route_realisations
import route_save_realisation
import route_delete_realisation
import route_configurations
import route_save_configuration
import route_delete_configuration
import route_pages
import route_squares
import route_page_detail




@app.route('/')
def index():
    return render_template('index.html')






if __name__ == '__main__':
    app.run(debug=True)