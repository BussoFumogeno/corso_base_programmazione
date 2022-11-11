doppio = 0

while True:
    numero = int (input("inserisci numero: "))

    if (numero %2==0):
        print ("pari")

    else:
        print ("dispari")

    if (doppio == numero):
        break

doppio = numero*2


