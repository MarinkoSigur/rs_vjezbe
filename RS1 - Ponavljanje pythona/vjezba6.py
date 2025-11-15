# 1. Napišite program koji ispisuje sumu svih parnih brojeva od 1 do 100 (uključivo).
suma = 0

for broj in range(1, 101):
    if broj % 2 == 0:
        suma += broj

print(f"Suma svih parnih brojeva od 1 do 100 je: {suma}")

# 2. Napišite program koji ispisuje prvih 10 neparnih brojeva u obrnutom redoslijedu.
neparni = []

broj = 0
while len(neparni) < 10:
    if broj % 2 != 0:
        neparni.append(broj)
    broj += 1

for n in reversed(neparni):
    print(n)


# 3. Napišite program koji ispisuje Fibonaccijev niz do 1000. Fibonaccijev niz počinje s brojevima 0 i 1, a
#    svaki sljedeći broj je zbroj prethodna dva broja.
a = 0 
b = 1

while a <= 1000:
    print(a)
    a, b = b, a + b
