from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    #user = {'username': 'Miguel'}
    #posts = [
    #    {
    #        'author': {'username': 'John'},
    #        'body': 'Beautiful day in Portland!'
    #    },
    #    {
    #        'author': {'username': 'Susan'},
    #        'body': 'The Avengers movie was so cool!'
    #    }
    #]
    return render_template('index.html')

#@app.route('/', methods=['POST'])
#def my_form_post():
#    text = request.form['text']
#    processed_text = text.upper()
#    return processed_text
