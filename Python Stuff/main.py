#create server
##ballslover69 will create a server
from multiprocessing import connection
import sqlite3

conn = sqlite3.connect('gay.db')

c = conn.cursor()


# Det er denne funksjonen som lager selve tablesene og putter dem i databasen.
def create_tables(conn):
    with connection:
        conn.execute()