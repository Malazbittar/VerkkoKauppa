ostoskori = []  # Alustetaan ostoskori tyhjäksi listaksi

# Määritellään tuotteet
tuote1 = {'nimi': 'Kahvi', 'hinta': 2.5}
tuote2 = {'nimi': 'Leipä', 'hinta': 1.5}
tuote3 = {'nimi': 'Maito', 'hinta': 1.0}

# Lisätään tuotteet ostoskoriin
ostoskori.append(tuote1)
ostoskori.append(tuote2)
ostoskori.append(tuote3)

# Tulostetaan ostoskorin sisältö
print("Ostoskorin sisältö:")
for tuote in ostoskori:
    print(tuote['nimi'], '-', tuote['hinta'], '€')
