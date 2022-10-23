min = float("inf")
max = float("-inf")
i = 0
while True:
    numero = int(input("inserisci numero: "))

    if (numero > max):
        max = numero

    if (numero < min):
        min = numero
     
    if (numero == 0):
        break
    
print (max)
print (min)
