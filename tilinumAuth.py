def tarkista_iban(tilinumero):
    
    tilinumero = tilinumero.replace(' ', '')
    
    # Tarkista pituus
    if len(tilinumero) != 18:
        return False
    
    # Siirrä maatunnus ja tarkistenumero loppuun
    tilinumero = tilinumero[4:] + tilinumero[:4]
    
    # Korvaa kirjaimet numeroilla
    tilinumero = ''.join(str(int(c, 36)) for c in tilinumero)
    
    # Laske jakojäännös
    jakojaannos = int(tilinumero) % 97
    
    #Tarkista jakojäännös
    return jakojaannos == 1


#ESIMERKKI TILINUMEROT
print(tarkista_iban('FI42 5000 1510 0000 23'))
print(tarkista_iban('FI55 2515 8869 5718 65'))
print(tarkista_iban('FI95 1786 3769 6731 97'))
print(tarkista_iban('FI07 5762 9588 4181 13'))
print(tarkista_iban('FI52 8592 6874 8382 54'))
print(tarkista_iban('SE76 9449 8965 5115 5139 7733'))
