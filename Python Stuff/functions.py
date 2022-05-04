#create server
##ballslover69 will create a server
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

    

y = ('bitch', 'ass', 'nword')
x = ["test_1 = 'velg'", "test_2 = 'med'", "test_3 = 'omhu'"]
x1 = ["test_1 = 'bitch'", "test_2 = 'ass'", "test_3 = 'nword'"]
pushing(y)
pulling(x1)