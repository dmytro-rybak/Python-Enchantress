from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def students():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'my_database'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students')
    results = [(name, surname, speciality_name) for (name, surname, speciality_name) in cursor]
    cursor.close()
    connection.close()
    return results


@app.route('/')
def index():
    return json.dumps({'students': students()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
