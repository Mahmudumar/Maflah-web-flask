from flask import Flask, render_template, request, redirect, url_for
from auto_msgs import THANK_MSG_4


app = Flask(__name__)

@app.route('/thank', methods=["GET", "POST"])
def thank():
    email = request.form.get('subscribe')
    print(email)
    return render_template('thank.html',msg=THANK_MSG_4)

@app.route('/', methods=["GET", "POST"])
def start():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
