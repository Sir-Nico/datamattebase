#create server
##ballslover69 will create a server
from multiprocessing import connection
import sqlite3

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api")
def home():
    return "Hello! this is the main page <h1>Hey<h1>"

if __name__ == "__main__":
    app.run()
    
    



#conn = sqlite3.connect('gay.db')

#c = conn.cursor()


# Det er denne funksjonen som lager selve tablesene og putter dem i databasen.
#def create_tables(conn):
    #with connection:
    #    conn.execute()