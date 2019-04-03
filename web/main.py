from flask import Flask, request
from classifier.src.classify import Classify
clf = Classify()
import json 

def make_response(age, pulse_rate, data):
    return json.dumps({
        'age': age,
        'pulse_rate': pulse_rate,
        'message': data
    })

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/classify-query")
def query():
    pulse_rate = request.args.get('pulse_rate')
    age = request.args.get('age')
    if not (pulse_rate and age):
        return make_response(age, pulse_rate, "pulse_rate and age are required")
    if not (is_number(pulse_rate) and is_number(age)):
        return make_response(age, pulse_rate, "both inputs must be numbers")
    inp_data = '%s %s' %(pulse_rate, age)
    _class = clf.pulse_classify_web(inp_data)
    return make_response(age, pulse_rate, _class)

@app.route("/classify-json", methods=['POST'])
def classify():
    if request.method != 'POST':
        return "method not allowed"
    data = request.get_json()
    pulse_rate = data['pulse_rate']
    age = data['age']
    if not (pulse_rate and age):
        return make_response(age, pulse_rate, "invalid input")
    inp_data = '%s %s' %(pulse_rate, age)
    _class = clf.pulse_classify_web(inp_data)
    return make_response(age, pulse_rate, _class)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')