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

# Creating a database and pointing the cursor to it
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

# Dropping the tabels if they exists so we can start fresh
cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Track')
cur.execute('DROP TABLE IF EXISTS Album')

# Creating the tables following the data model and schema
cur.execute('''CREATE TABLE Artist 
            (id INTEGER NOT NULL PRIMARY KEY, name TEXT UNIQUE)''')

cur.execute('''CREATE TABLE Genre 
            (id INTEGER NOT NULL PRIMARY KEY, name TEXT UNIQUE)''')

cur.execute('''CREATE TABLE Album 
            (id INTEGER NOT NULL PRIMARY KEY, artist_id INTEGER, title TEXT UNIQUE)''')

cur.execute('''CREATE TABLE Track 
            (id INTEGER NOT NULL PRIMARY KEY , 
            title TEXT UNIQUE,
            album_id INTEGER, 
            genre_id INTEGER,
            len INTEGER, rating INTEGER, count INTEGER)''')

# Parse the data from the csv and insert it into the tables
handle = open ('../files/tracks.csv')
for line in handle:
    line = line.strip()
    pieces = line.split(',')
    
    if len(pieces) < 6 : continue

    # Extract each field of interest from the csv
    title = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    # Insert the Artist data into its table
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    # Get the id of the current artist being inserted in this iteration
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    # Retrieve the id of the artist
    artist_id = cur.fetchone()[0]
    
    # Insert the Album data into its table, use the artist_id as a foreign key
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
    # Get the id of the current album being inserted in this iteration
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    # Retrieve the id of the artist
    album_id = cur.fetchone()[0]
    
    # Insert the Genre data into its table
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    #Get the id of the current genre being inserted in this iteration
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    # Retrieve the id of the genre
    genre_id = cur.fetchone()[0]



    cur.execute('''INSERT OR REPLACE INTO Track 
            (title, album_id, genre_id, len, rating, count) VALUES (?,?,?,?,?,?)''',
            (title, album_id, genre_id, length, rating, count))
    
    conn.commit()

    # What we want to see
    # The tables wich hold the data
    # How the tables are linked

cur.execute('''
            SELECT Track.title, Artist.name, Album.title, Genre.name 
            FROM Track JOIN Genre JOIN Album JOIN Artist 
            ON Track.genre_id = Genre.id and Track.album_id = Album.id 
            AND Album.artist_id = Artist.id 
            ORDER BY Artist.name LIMIT 3''')
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

cur.execute('''SELECT * FROM Album LIMIT 10''')
for row in cur: print(row)

cur.execute('''SELECT * FROM Track JOIN Album ON Track.album_id = Album.id
            JOIN Artist ON Album.artist_id = Artist.id 
            JOIN Genre ON Track.genre_id = Genre.id
            LIMIT 2''')
for row in cur: print(row)

cur.execute('DELETE FROM Track')
cur.execute('DELETE FROM Artist')
cur.execute('DELETE FROM Album')
cur.execute('DELETE FROM Genre')
cur.close()