from flask import render_template, request
from app import app
import operator_aware_lib_v1

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def dummmy():
    x = request.form['Item_1']
    OA_eval = operator_aware_lib_v1.evaluate_call(x)
    return OA_eval
