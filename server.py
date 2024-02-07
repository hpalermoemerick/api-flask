from flask import Flask, request, jsonify, render_template, redirect
import handle_mysql

app = Flask(__name__)

# get datas to connect to MySQl
global cursor
global connectDB
cursor, connectDB = handle_mysql.makeConnection()

def getPeople(cursor, connectDB):
    querySQL = "SELECT * FROM pessoa"
    listaPessoas = handle_mysql.readData(querySQL, cursor)
    return listaPessoas

@app.route('/addPerson', methods=['GET'])
def addPerson():
    return render_template('addPerson.html')

@app.route('/', methods=['GET'])
def index():
    listaPessoas = []
    listaPessoas = getPeople(cursor, connectDB)

    return render_template('index.html', listaPessoas=listaPessoas)

@app.route('/save-person', methods=['POST'])
def savePerson():
    data = request.get_json()
    print(data)
    handle_mysql.createData(data, cursor, connectDB)

    return jsonify({ "url" : "/" })

@app.route('/update/<int:id>', methods=['GET', 'PUT'])
def updatePersonGet(id):
    if request.method == 'GET':
        querySQL = f"SELECT * FROM pessoa WHERE id = {id}"
        pessoa = handle_mysql.readData(querySQL, cursor)
        print(pessoa)
        return render_template('updatePerson.html', pessoa=pessoa)
    else:
        data = request.get_json()
        querySQL = "UPDATE pessoa SET nome = %s, idade = %s, email = %s WHERE id = %s"
        values = (data.get('nome'), data.get('idade'), data.get('email'), id)  # Supondo que 'id' seja obtido de alguma forma

        handle_mysql.updateData(querySQL, values, cursor, connectDB)
        
        return jsonify({ "url" : "/" })

@app.route('/delete/<int:id>', methods=['DELETE'])
def deletePerson(id):
    querySQL = f"DELETE FROM pessoa WHERE id = {id}"
    handle_mysql.deleteData(querySQL, cursor, connectDB)
    
    return jsonify({ "url" : "/" })


app.run(debug=True)