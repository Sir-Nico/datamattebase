#create server
##ballslover69 will create a server
import sqlite3

conn = sqlite3.connect('eksempel.db')

c = conn.cursor()

def pulling(search_list, output_list):
    output_list.clear()
    search_string = "SELECT * FROM tasks WHERE "
    for term in search_list:
        search_string += f"{term} AND "
    search_string = search_string[:-5]
    c.execute(search_string)
    items = c.fetchall()
    for item in items:
        output_list.append(item)



#   denne funksjonen finner items fra en liste med sql kommandoer i string format, og plasserer dem i en output liste

def pushing(insert_list):
    command_string = "INSERT INTO tasks VALUES ("
    for term in insert_list:
        command_string += f"'{term}', "
    command_string = command_string[:-2]
    command_string += ")"
    c.execute(command_string)
    conn.commit()
    
#   denne funksjonen inserter items fra en liste i tasks tabelet



#   search_list må være en liste variabel med string items i formatet search_list = ["test_1 = 'eksempel1'", "test_2 = 'eksempel2'", "test_3 = 'eksempel3'"]
#   output_list er en liste med itemsa funnet med pulling funksjonen. den cleares på starten av funksjonen, så ta med deg informasjonen til en annen variabel hvis du skal kjøre den flere ganger
#   insert_list er en variabel av det du vil sette inn i tabelet. skriv det i formatet insert_list = ('eksempel1', 'eksempel2', 'eksempel3')

