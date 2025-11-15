# Pojasnite zašto sljedeća petlja nema (previše) smisla:
for i in range(1, 2):
    print(i)

#Petlja će se izvršiti samo jednom što nema smisla jer for petlje se obično koriste za višestruka ponavljanja.



#Što će ispisati sljedeća petlja?
for i in range(10, 1, 2):
    print(i)

#Pokazati će grešku jer je korak definiran kao pozitivan odnosno da brojimo prema naprijed, a početna i zadnja vrijednost su takve da možemo samo brojati unazad


#Što će ispisati sljedeća petlja?
for i in range(10, 1, -1):
    print(i)
#Ispisat će brojeve od 10 do 2 unazad