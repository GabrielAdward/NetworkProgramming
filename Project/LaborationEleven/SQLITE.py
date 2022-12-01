import sqlite3

conn = sqlite3.connect("Databaswname")
c = conn.cursor()

c.execute(""" """)

test = open(r"C:\Users\gabri\OneDrive\Dokument\GitHub\NetworkProgramming\Project\LaborationTwo\score2.txt", "r")

for row in c.execute("Query "):
    print(row)

conn.commit()
conn.close()