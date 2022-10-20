somma = 0
i = 0

while True:
    numero = int(input("inserisci un numero: "))

    if ( numero == 0):
        break
    
    else:
        somma = somma + numero
    
    i = i + 1

print (somma/i)