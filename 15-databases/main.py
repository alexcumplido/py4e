"""
Do not replicate data - reference data - point at data
Use integers for keys and for references
Add a special "key" column to each table wch we will make reference to

Primary key : generally  integer auto-incremented field
Logical key : what the outside world uses for lookup (never use as primary key, they can change)
Foreign key: generally an integer key pointing to a row in another table

A foreign key is when a table has a column that contains a key wich points to the primary key of another table
When all primary keys are integers, all foreign keys are integers
Avoid vertical replication of strings (vertical axis)
"""
import sqlite3 

conn = sqlite3.connect('music.sqlite')

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Track')
cur.execute('DROP TABLE IF EXISTS Album')

cur.execute('''CREATE TABLE Artist 
            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE)''')

cur.execute('''CREATE TABLE Genre 
            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE)''')

cur.execute('''CREATE TABLE Album 
            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id INTEGER, title TEXT UNIQUE)''')

cur.execute('''CREATE TABLE Track 
            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
            title TEXT UNIQUE,
            album_id INTEGER, 
            genre_id INTEGER,
            len INTEGER, rating INTEGER, count INTEGER)''')

handle = open ('../files/tracks.csv')
for line in handle:
    line = line.strip()
    pieces = line.split(',')
    
    if len(pieces) < 6 : continue

    title = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]
    
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]
    
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id,))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]
    
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track 
            (title, album_id, genre_id, len, rating, count) VALUES (?,?,?,?,?,?)
            ''',(title, album_id, genre_id, length, rating, count))
    conn.commit()

    # What we want to see
    # The tables wich hold the data
    # How the tables are linked

cur.execute('''
            SELECT Track.title, Artist.name, Album.title, Genre.name 
            FROM Track JOIN Genre JOIN Album JOIN Artist 
            ON Track.genre_id = Genre.id and Track.album_id = Album.id 
            AND Album.artist_id = Artist.id 
            ORDER BY Artist.name LIMIT 30''')
for row in cur: print(row)

cur.execute('''SELECT Album.title, Artist.name 
            FROM Album JOIN Artist 
            ON Album.artist_id = Artist.id''')
for row in cur: print(row)

cur.execute('''SELECT Album.title, Album.artist_id, Artist.id, Artist.name
            FROM Album JOIN Artist
            ON Album.artist_id = Artist.id''')
for row in cur: print(row)

cur.execute('''SELECT Track.title, Genre.name
            FROM Track JOIN Genre
            ON Track.genre_id =  Genre.id''')
for row in cur: print(row)


cur.execute('DELETE FROM Track')
cur.execute('DELETE FROM Artist')
cur.execute('DELETE FROM Album')
cur.execute('DELETE FROM Genre')
cur.close()