from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def library_data():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'library'  # Certifique-se de que este nome está correto
    }
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT Autor, Title FROM books')
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results
    except mysql.connector.Error as err:
        # Log ou imprima o erro para depuração
        print("Database error:", err)
        return []

@app.route('/')
def index():
    return jsonify({'Library Data': library_data()})

if __name__ == '__main__':
    app.run(host='0.0.0.0')