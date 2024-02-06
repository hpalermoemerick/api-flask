from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/addPerson', methods=['GET'])
def addPerson():
    return render_template('addPerson.html')

app.run(debug=True)