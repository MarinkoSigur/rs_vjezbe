#1. Funkcija koja vraća n-torku s prvim i zadnjim elementom liste u jednoj liniji koda.

def prvi_i_zadnji(lista): 
    return (lista[0], lista[-1])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prvi_i_zadnji(lista))

#2. Funkcija koja vraća n-torku s maksimalnim i minimalnim elementom liste, bez korištenja ugrađenih funkcija max() i min().

def maks_i_min(lista):
    najmanji = lista[0]
    najveci = lista[0]

    for broj in lista:
        if broj < najmanji:
            najmanji = broj
        if broj > najveci:
            najveci = broj

    return (najveci, najmanji)

lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista))


#3. Funkcija presjek koja prima dva skupa i vraća novi skup s elementima koji se nalaze u oba skupa.

def presjek(skup1, skup2):
    return skup1.intersection(skup2)

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print(presjek(skup_1, skup_2))