import sqlite3
def databasePython():
    conn = sqlite3.connect("test1.db")
    c = conn.cursor()

    c.execute('PRAGMA foreign_keys = ON')
    
    c.execute(""" Create table IF NOT EXISTS persons(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name1 TEXT,
        name2 TEXT
    );""")

    c.execute(""" Create table IF NOT EXISTS scores(
        idPerson INTEGER,
        task INTEGER,
        score INTEGER,
        FOREIGN KEY (idPerson) REFERENCES persons(id) ON DELETE CASCADE
    );""")

    for x in open(r"C:\Users\gabri\OneDrive\Dokument\GitHub\NetworkProgramming\Project\LaborationEleven\score2.txt", "r").readlines():
        content = x.strip().split(" ")
        c.execute("INSERT INTO persons (name1, name2) VALUES (?,?);", (content[2], content[3]))
        
    for i in open(r"C:\Users\gabri\OneDrive\Dokument\GitHub\NetworkProgramming\Project\LaborationEleven\score2.txt", "r").readlines():
        content = i.strip().split(" ")
        for y in c.execute('SELECT id from persons WHERE name1 = ? and name2 = ?', (content[2], content[3])):
            c.execute('INSERT INTO scores (idPerson , task, score) VALUES (?,?,?)', (y[0], content[1], content[4]))

    #(a) List the 10 p ersons who have the highest numb er of total points.
    #DESC sort the highest first
    print(c.execute(""" SELECT name1 || " " || name2, 
                    sum(score) FROM scores
                    JOIN persons ON persons.id = scores.idPerson
                    group by id 
                    order by SUM(score) DESC
                    limit(10);
                    """).fetchall())
    
    #(b) List the 10 most dicult tasks, that is, the 10 tasks which have minimal total points.
    print(c.execute("""
                    SELECT task, sum(score) FROM scores
                    group by task
                    order by SUM(score) asc
                    limit(10);
                    """).fetchall())
    
    conn.commit()
    conn.close()
databasePython()
