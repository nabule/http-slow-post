from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def welcome():
    return "Hi "+ request.form['name']

app.run(host='0.0.0.0', threaded=True)