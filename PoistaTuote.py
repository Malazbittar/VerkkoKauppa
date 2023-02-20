import sqlite3

# Yhdistetään tietokantaan
conn = sqlite3.connect('tuoteluettelo.db')
c = conn.cursor()

# Kysytään käyttäjältä poistettavan tuotteen id-numero
tuote_id = int(input("Syötä poistettavan tuotteen id-numero: "))

# Tarkistetaan, onko tuote olemassa tietokannassa
c.execute("SELECT * FROM tietokoneet WHERE id=?", (tuote_id,))
tuote = c.fetchone()
if tuote is None:
    print("Tuotetta ei löydy tuoteluettelosta")
else:
    # Poistetaan tuote tietokannasta
    c.execute("DELETE FROM tietokoneet WHERE id=?", (tuote_id,))
    conn.commit()
    print("Tuote on poistettu tuoteluettelosta")

# Suljetaan tietokantayhteys
conn.close()
