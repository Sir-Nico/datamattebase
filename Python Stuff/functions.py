import sqlite3

conn = sqlite3.connect('eksempel.db')

c = conn.cursor()

def pulling(x):
    search_string = "SELECT * FROM tasks WHERE "
    for term in x:
        search_string += f"{term} AND "
 
    search_string = search_string[:-5]
    print("test")
    c.execute(search_string)
    items = c.fetchall()
    for item in items:
        print(item)

def pushing(y):
    command_string = f"INSERT INTO tasks VALUES {y}"
    print(command_string)
    try:
        c.execute(command_string)
        conn.commit()
    except Exception as e:
        print(e)
