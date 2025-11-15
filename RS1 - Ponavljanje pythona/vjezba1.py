broj_1 = float(input("unesite broj 1:"))
broj_2 = float(input("unesite broj 2:"))

operator = input("unesite operator (+, -, *, /):")
if operator == "+":
    rezultat = broj_1 + broj_2
elif operator == "-":
    rezultat = broj_1 - broj_2  
elif operator == "*":
    rezultat = broj_1 * broj_2
elif operator == "/":
    if broj_2 != 0:
        rezultat = broj_1 / broj_2
    else:
        rezultat = "Greška: Dijeljenje s nulom nije dozvoljeno."
else:
    rezultat = "Greška: Nepoznat operator." 
print("Rezultat:", rezultat)
    