import sqlite3

# Yhdistetään tietokantaan
conn = sqlite3.connect('tuoteluettelo.db')
c = conn.cursor()

# Luodaan taulu, jos sitä ei ole vielä olemassa
c.execute('''CREATE TABLE IF NOT EXISTS tietokoneet
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             merkki TEXT,
             malli TEXT,
             hinta REAL)''')

# Kysytään käyttäjältä tietokoneen tiedot
merkki = input("Syötä tietokoneen merkki: ")
malli = input("Syötä tietokoneen malli: ")
hinta = float(input("Syötä tietokoneen hinta: "))

# Lisätään tietokantaan uusi tietokone
c.execute("INSERT INTO tietokoneet (merkki, malli, hinta) VALUES (?, ?, ?)", (merkki, malli, hinta))
conn.commit()

# Tulostetaan lisätyn tietokoneen tiedot
print("Uusi tietokone on lisätty tietokantaan:\nMerkki:", merkki, "\nMalli:", malli, "\nHinta:", hinta)

# Suljetaan tietokantayhteys
conn.close()
