import sqlite3
import json


file = open('../files/roster_data.json')
data = json.load(file)
# Create a database and point a cursos to it
conn = sqlite3.connect('courses.sqlite')
cur = conn.cursor()

# Drop tables if they exist so we can start fresh
cur.execute('DROP TABLE IF EXISTS Course')
cur.execute('DROP TABLE IF EXISTS User')
cur.execute('DROP TABLE IF EXISTS Role')
cur.execute('DROP TABLE IF EXISTS Member')

# Create tables with the schema and unique constraints
cur.execute('''CREATE Table User
            (id INTEGER NOT NULL PRIMARY KEY UNIQUE, name TEXT UNIQUE)
            ''')   

cur.execute('''CREATE TABLE Course 
            (id INTEGER NOT NULL PRIMARY KEY UNIQUE, title TEXT UNIQUE)
            ''')

cur.execute('''CREATE TABLE Role
            (id INTEGER NOT NULL PRIMARY KEY UNIQUE, name TEXT UNIQUE)
            ''')

# Create a transition table  (many to many connector table) to handle the many to many relationship
# Known as well as juntion table
cur.execute('''CREATE TABLE Member
            (user_id INTEGER, 
            course_id INTEGER, 
            role_id INTEGER, 
            PRIMARY KEY (user_id, course_id, role_id))
            ''') 

# Iterate over the data and insert it into the tables
for entry in data:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    # print((name, title, role))

    # Insert the name of the user
    # Retrieve the id of the user inserted
    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''',(name,))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = cur.fetchone()[0]

    # Insert the title of the course
    # Retrieve the id of the course inserted
    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''',(title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    # Insert the role of the course
    # Retrieve the id of the role inserted
    cur.execute('''INSERT OR IGNORE INTO Role (name) VALUES (?)''', (role,))
    cur.execute('SELECT id FROM Role WHERE name = ?', (role,))
    role_id = cur.fetchone()[0]

    # Insert the user_id and the course_id into the Member table (transition table)
    # Junction table
    cur.execute('''INSERT OR REPLACE INTO Member
                (user_id, course_id, role_id) VALUES (?, ?, ?)''', (user_id, course_id, role_id))

    conn.commit()

# cur.execute('''SELECT * FROM Course
#             JOIN Member ON Course.id = Member.course_id
#             JOIN User ON Member.user_id = User.id
#             JOIN Role ON Member.role_id = Role.id
# ''')
# for row in cur: print(row)

cur.execute('''
            SELECT User.name, Course.title, Role.name FROM User
            JOIN Member ON User.id = Member.user_id 
            JOIN Course ON Member.course_id = Course.id
            JOIN Role ON Member.role_id = Role.id 
            ORDER BY User.name DESC, Course.title DESC, Role.name DESC LIMIT 2
''')
for row in cur: print(row)

cur.execute('''
           SELECT 'XYZZY' || hex(User.name || Course.title || Role.name ) AS X FROM User
            JOIN Member ON User.id = Member.user_id
            JOIN Role ON Member.role_id = Role.id
            JOIN Course ON Member.course_id = Course.id
            ORDER BY X LIMIT 1
''')
for row in cur: print(row)

cur.execute('DELETE FROM User')
cur.execute('DELETE FROM Course')
cur.execute('DELETE FROM Role')
cur.execute('DELETE FROM Member')
conn.close()