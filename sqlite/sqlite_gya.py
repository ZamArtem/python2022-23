import sqlite3

con = sqlite3.connect("ujbase.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS kutya")

cur.execute("CREATE Table kutya(nem, szin)")
con.commit()
valtozo = 0

cur.execute(""" 
    INSERT INTO kutya VALUES
        ('Ferfi', 'fekete'),
        ('No','sarga'),
        ('Ferfi','feher');""")
con.commit()

res = cur.execute("SELECT nem FROM kutya")
print(res.fetchall())