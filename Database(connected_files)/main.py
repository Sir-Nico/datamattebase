#create server
##ballslover69 will create a server
from ast import dump
from crypt import methods
from multiprocessing import connection
import sqlite3

from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")
    #return "hey there"
    


if __name__ == "__main__":
    app.run(debug = True)


    
    



#conn = sqlite3.connect('gay.db')

#c = conn.cursor()


# Det er denne funksjonen som lager selve tablesene og putter dem i databasen.
#def create_tables(conn):
    #with connection:
    #    conn.execute()