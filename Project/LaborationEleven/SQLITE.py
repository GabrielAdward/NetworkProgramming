import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()

c.execute('PRAGMA foreign_keys = ON')
c.execute(""" Create table IF NOT EXIST persons(
    personID INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT,
    lastname TEXT)""")

c.execute(""" Create table IF NOT EXIST scores(
    id INTEGER,
    task INTEGER,
    score INTEGER,
    FOREIGN KEY (idPerson) REFERENCES persons(id) ON DELETE CASCADE
)""")

#for x in open("score2.txt").readlines():
    
#for x in open ("score2.txt").readlines():

conn.commit()
conn.close()