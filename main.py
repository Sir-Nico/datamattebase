#create server
##ballslover69 will create a server
import sqlite3

conn = sqlite3.connect('gay.db')

c = conn.cursor()

def pulling(x):
    search_string = "SELECT * FROM ((table)) WHERE "
    for term in x:
        search_string += f"condition='{x}' AND "
    search_string = search_string[:-5]
    c.execute(search_string)
    items = c.fetchall()
    for item in items:
        print(item)

x = []
