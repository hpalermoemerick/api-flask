import mysql.connector

connectDB = None
cursor = None

# close connetions
# ??? --------------------------------------- ???
#   def closeConnection(cursor, connectDB):
#        cursor.close()
#        connectDB.close()
# ??? --------------------------------------- ???

def createData(data, cursor, connectDB):
    nome = data.get('nome')
    idade = data.get('idade')
    email = data.get('email')

    querySQL = f"INSERT INTO pessoa (nome, idade, email) VALUES ('{nome}', {idade}, '{email}');"
    cursor.execute(querySQL)
    connectDB.commit() # when edit database


def readData(querySQL, cursor):
    cursor.execute(querySQL)
    result = cursor.fetchall() # read the database
    return result

def updateData(querySQL, values, cursor, connectDB):
    cursor.execute(querySQL, values)
    connectDB.commit() # when edit database

def deleteData(querySQL, cursor, connectDB):
    cursor.execute(querySQL)
    connectDB.commit() # when edit database

# CRUD
def makeConnection():
    connectDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="CRUD_Pessoa"
    )
    cursor = connectDB.cursor()
    return cursor, connectDB





# chove chove