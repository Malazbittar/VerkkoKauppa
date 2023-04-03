
"""
Verkkokuppa prjokti

"""
import sqlite3

db = sqlite3.connect("kauppa.db")
db.isolation_level = None

def luo_tuotteen_taulu():
    try:
        db.execute("CREATE TABLE tuotteet(id INTEGER PRIMARY KEY, nimi TEXT, hinta INTEGER, kuvaus TEXT)")
    except:
        print("Taulu on jo luotu")

def lisaa_tuotteet(nimi, hinta, kuvaus):
    db.execute("INSERT INTO tuotteet(nimi, hinta, kuvaus) \
                VALUES(?,?,?)",[nimi, hinta, kuvaus])
    
def poista_tuote(id):
    db.execute("DELETE FROM tuotteet WHERE id = ?", [id])
 

def main():
    luo_tuotteen_taulu()
    print("""1 - Lisää tuotteet
2 - Poista tuote    
0 - Lopeta""")
    while True:
        komento = input("Anna komento: ")
        if komento == "0":
            print('\nKiitos ohjelmiston käytöstä!\n')
            break
        
        if komento == "1":
            nimi = input("Anna tuoten nimi: ")
            hinta = int(input("Anna tuoten hinta : "))
            kuvaus = input("Anna tuoten kuvaus: ")
            lisaa_tuotteet(nimi, hinta, kuvaus)

        if komento == "2":
            id = input("Anna poistettavan tuotteen ID: ")
            poista_tuote(id)
            print("Tuote on poistettu")
            
            	
if __name__=="__main__":
	main() 
