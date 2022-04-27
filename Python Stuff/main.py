#create server
##ballslover69 will create a server
from multiprocessing import connection
import sqlite3

from flask import Flask, request, jsonify, after_this_request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    jsonResp = {'jack': 4098, 'sape': 4139}
    print(jsonResp)
    return jsonify(jsonResp)

if __name__ == '__main__':
    app.run(host='localhost', port=8989)



conn = sqlite3.connect('gay.db')

c = conn.cursor()


# Det er denne funksjonen som lager selve tablesene og putter dem i databasen.
def create_tables(conn):
    with connection:
        conn.execute()