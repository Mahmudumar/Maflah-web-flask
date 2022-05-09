from flask import Flask, render_template, request, redirect, url_for
import flask
from flask.templating import render_template_string


app = Flask(__name__)
@app.route('/')
def products():
    return render_template_string()

@app.route('/thank', methods=["GET", "POST"])
def thank():
    email = request.form.get('subscribe')
    print(email)
    
    return render_template('thank.html')

@app.route('/', methods=["GET", "POST"])
def start():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
