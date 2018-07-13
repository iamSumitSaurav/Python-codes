import sqlite3
database = sqlite3.connect('firstDatabase.db')

sql = "SELECT * FROM Players;"
cur = database.cursor()
cur.execute(sql)
while True:
    record = cur.fetchone()
    if record == None:
        break
    print(record)
