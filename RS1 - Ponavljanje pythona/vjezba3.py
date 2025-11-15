tajni_broj = 147
pogodjen = False
pokusaja = 0
while not pogodjen:
    unos = int(input("Pogodi tajni broj (između 1 i 200): "))
    pokusaja += 1
    if unos < tajni_broj:
        print("Tvoj unos je manji od tajnog broja.")
    elif unos > tajni_broj:
        print("Tvoj unos je veći od tajnog broja.")
    else:
        print(f"Čestitamo! Pogodili ste tajni broj u {pokusaja} pokušaja.")
        pogodjen = True