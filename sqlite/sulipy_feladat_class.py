import sqlite3

#year;programming language;first name; last name of chief developer
#1972;C;Dennis; Ritchie

class Adatbazis:
    def __init__(self,sor):
        ev,nyelv,nev,csaladnev = sor.strip().split(";")
        self.ev         = ev
        self.nyelv      = nyelv
        self.nev        = nev
        self.csaladnev  = csaladnev


with open("nevek.txt")as f:
    cimke = f.readline()
    lista = [Adatbazis(sor) for sor in f]


con = sqlite3.connect("feladat.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS programozok")
cur.execute("CREATE TABLE programozok(ev, nyelv, nev, csaladnev) ")

for i in lista:
    data = [(i.ev,i.nyelv,i.nev,i.csaladnev)]
    cur.executemany("INSERT INTO programozok VALUES(?, ?, ?, ?)", data)


con.commit()
res = cur.execute("SELECT nyelv,nev FROM programozok")
print(res.fetchall())

        