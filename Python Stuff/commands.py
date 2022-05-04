import sqlite3


def create_table(c):
    c.execute("""CREATE TABLE tasks(
        test_1 TEXT,
        test_2 TEXT,
        test_3 TEXT
    )""")


def main():
    conn = sqlite3.connect("eksempel.db")
    c = conn.cursor()
    c.execute("INSERT INTO tasks VALUES ('velg', 'med', 'omhu')")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()


