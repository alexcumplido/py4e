import sqlite3 
conn = sqlite3.connect('ages.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name TEXT, age, INTEGER)')


data_ages = [('Karrah', 14), ('Taliesin', 14), ('Lauryn', 40), ('Oluwatosin', 26), ('Nitya', 40), ('Candice', 36)]

for name, age in data_ages:
    cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', (name, age))
conn.commit()
cur.execute('SELECT name, age FROM Ages')
for row in cur: print(row)

cur.execute('DELETE FROM Ages')
conn.commit()
cur.close()
