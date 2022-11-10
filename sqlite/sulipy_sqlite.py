import sqlite3


con = sqlite3.connect("tutorial.db")

cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS filmek")
cur.execute("CREATE TABLE filmek(cim, ev, ertekeles)")

cur.execute("""
    INSERT INTO filmek VALUES
    ("A pokemer", 2022, 8.1),
    ("A felhokarcolo", 2021, 8.9);
""")
con.commit()
res = cur.execute("SELECT * FROM filmek")
print(res.fetchall())
con.close()


