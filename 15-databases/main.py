import sqlite3 

conn = sqlite3.connect('email.sqlite')

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Users')
cur.execute('CREATE TABLE Users (name TEXT, email TEXT)')

cur.execute('INSERT INTO Users (name, email) VALUES (?, ?)',('Chuck', 'csev@umich.edu'))
cur.execute('INSERT INTO Users (name, email) VALUES (?, ?)', ('Colleen', 'cvl@umich.edu'))
cur.execute('INSERT INTO Users (name, email) VALUES (?, ?)', ('Ted', 'ted@umich.edu'))
cur.execute('INSERT INTO Users (name, email) VALUES (?, ?)', ('Sally', 'a1@umich.edu'))
cur.execute('INSERT INTO Users (name, email) VALUES (?, ?)', ('Ted', 'ted@umich.edu'))
cur.execute('INSERT INTO Users (name, email) VALUES (?, ?)', ('Kristen', 'kf@umich.edu'))
conn.commit()

print('Track:')
# cur.execute('SELECT title, plays FROM Track ORDERED BY title')
# cur.execute('SELECT * FROM Track WHERE title = "My Way')
# cur.execute('SELECT title, plays FROM Track ORDERED BY title')
# cur.execute('UPDATE Track SET plays = 16 WHERE title = "My Way"')
conn.commit()

cur.execute('SELECT name, email FROM Users')
for row in cur: 
    print(row)

cur.execute('DELETE FROM Users')
conn.commit()
cur.close()

