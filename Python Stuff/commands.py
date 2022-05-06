import sqlite3
from functions import *


# Function that creates an example table (modify to your needs)
def create_table(c):
    c.execute("""CREATE TABLE tasks(
        test_1 TEXT,
        test_2 TEXT,
        test_3 TEXT
    )""")

# Main function, runs SQL Commands, currently inserting data into the example database
# Again, modify to your needs, just remember to update the comments
def main():
    conn = sqlite3.connect("eksempel.db")
    c = conn.cursor()
    c.execute("INSERT INTO tasks VALUES ('velg', 'med', 'omhu')")
    conn.commit()
    conn.close()

# Runs the main function if the program is being ran as __main__
# (not imported, ran directly)
if __name__ == "__main__":
    main()


