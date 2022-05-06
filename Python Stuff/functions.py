import sqlite3

conn = sqlite3.connect('eksempel.db')

c = conn.cursor()

def pulling(x, z):
    search_string = "SELECT * FROM tasks WHERE "
    for term in x:
        search_string += f"{term} AND "
 
    search_string = search_string[:-5]
    print("test")
    c.execute(search_string)
    items = c.fetchall()
    for item in items:
        z.append(item)

def pushing(y):
<<<<<<< HEAD
    command_string = f"INSERT INTO tasks VALUES {y}"
    print(command_string)
    try:
        c.execute(command_string)
        conn.commit()
    except Exception as e:
        print(e)
=======
    command_string = "INSERT INTO tasks VALUES ("
    for term in y:
        command_string += f"'{term}', "
    command_string = command_string[:-2]
    command_string += ")"
    c.execute(command_string)
    conn.commit()
    



    
#   z = []
#   bytt z med en liste variabel der du vil at tingene du søker etter skal bli displaya (husk å cleare den)

#   y = ('something1', 'something2', 'something3')
#   bytt med en variabel der something(1, 2, 3) er hva du vil ha i de respektive columnsa 

#   x = ["test_1 = 'something1'", "test_2 = 'something2'", "test_3 = 'something3'"]
#   bytt something(1, 2, 3) med en liste over columnsa, og hvilke item i de columnsa du vil søke etter
>>>>>>> ea166b6fd031ad8cd39f20354d349920bbbed095
