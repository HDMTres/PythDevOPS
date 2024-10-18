from flask import Flask, jsonify, request
from fonct import add_numbers, supp_numbers, multy_numbers, diff_numbers

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    result = add_numbers(data['a'], data['b'])
    return jsonify({"result": result})

@app.route('/subtract', methods=['POST'])
def supp():
    data = request.json
    result = supp_numbers(data['a'], data['b'])
    return jsonify({"result": result})

@app.route('/multy', methods=['POST'])
def multy():
    data = request.json
    result = multy_numbers(data['a'], data['b'])
    return jsonify({"result": result})

@app.route('/diff', methods=['POST'])
def diff():
    data = request.json
    result = diff_numbers(data['a'], data['b'])
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
