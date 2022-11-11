doppio = 0
i = 0
while ( i <= 10):
    numero = int(input("inserisci un numero: "))
    
    if (numero %2==0):
        print("pari")
    else:
        print("dispari")

    if (doppio == numero):
        break
    doppio = numero*2
    i = i + 1