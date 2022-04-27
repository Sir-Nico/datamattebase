#create server
from multiprocessing import connection
import sqlite3



# Det er denne funksjonen som lager selve tablesene og putter dem i databasen.
def create_tables(connection):
    with connection:
        connection.execute()