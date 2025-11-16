from shop import proizvodi

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

def dodaj_proizvod(proizvodi_za_dodavanje):
    for proizvod in proizvodi_za_dodavanje:
        proizvodi.dodaj_proizvod(
            proizvod["naziv"],
            proizvod["cijena"],
            proizvod["dostupna_kolicina"]
        )

print(proizvodi_za_dodavanje)
