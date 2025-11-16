class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        return f"Proizvod: {self.naziv}, Cijena: {self.cijena} EUR, Dostupna količina: {self.dostupna_kolicina}"
    
skladiste = [
    Proizvod("Slusalice", 149.99, 10),
    Proizvod("Tablet", 139.99, 25),
]

def dodaj_proizvod(naziv, cijena, dostupna_kolicina):
    novi_proizvod = Proizvod(naziv, cijena, dostupna_kolicina)
    skladiste.append(novi_proizvod)