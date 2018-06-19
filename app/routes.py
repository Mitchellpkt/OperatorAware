from flask import render_template, request
from app import app
from operator_aware_lib.handler_in_str_to_out_str import handler_in_str_to_out_str

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def dummmy():
    x = request.form['Item_1']
    OA_eval = handler_in_str_to_out_str(x)
    return OA_eval
