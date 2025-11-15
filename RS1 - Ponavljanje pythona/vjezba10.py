tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

def brojanje_riječi(tekst):
    rijeci = tekst.lower().split()   
    ponavljanje = {}                 

    for rijec in rijeci:
        if rijec in ponavljanje:
            ponavljanje[rijec] += 1  
        else:
            ponavljanje[rijec] = 1  
    
    return ponavljanje

print(brojanje_riječi(tekst))