import sqlite3

con = sqlite3.connect("feladat.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS programozok")
cur.execute("CREATE TABLE programozok(ev, nyelv, nev, csaladnev) ")
data = [
    (1972,"C","Dennis", "Ritchie"),
    (1964,"BASIC","John George","Kemeny"),
    (1964,"BASIC","Thomas Eugene","Kurtz"),
    (1995,"Java","James","Gosling"),
    (1983,"C++","Bjarne","Stroustrup"),
    (1987,"Perl","Larry","Wall"),
    (1995,"JavaScript","Brendan","Eich"),
    (1970,"Pascal","Niklaus","Wirth"),
    (1946,"ENIAC Short Code","Richard","Clippinger"),
    (1946,"ENIAC Short Code","John","von Neumann"),
    (1995,"PHP","Rasmus","Lerdorf"),
    (1989,"Python","Guido","Van Rossum"),
    (2000,"C#","Anders","Hejlsberg"),
    (1970,"Pascal","Kathleen","Jensen")
]

cur.executemany("INSERT INTO programozok VALUES(?, ?, ?, ?)", data)
con.commit()
res = cur.execute("SELECT nyelv,nev FROM programozok")
print(res.fetchall())
