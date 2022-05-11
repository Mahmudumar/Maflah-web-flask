import time
from flask import Flask, redirect, render_template, request


THANK_MSG_1="Thank you"
THANK_MSG_2="Thank you. You are the best"
THANK_MSG_3="Thank you. You are breathtaking"
THANK_MSG_4="Thank you. We've received your email. We will let you know when our website's complete"


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
    
