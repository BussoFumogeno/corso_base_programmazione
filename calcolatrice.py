def somma (a,b):
    return a + b
def sottrazione (a,b):
    return a - b
def moltiplicazione (a,b):
    return a * b
def divisione (a,b):
    return a / b

while True:
    n1 = int(input("inserisci un numero: "))
    n2 = int(input("inserisci un numero: "))

    segno = str(input("inserisci l'operazione che vuoi svolgere: "))
    if (segno == "somma"):
        print (somma (n1,n2))

    if (segno == "sottrazione"):
        print (sottrazione (n1,n2))

    if (segno == "moltiplicazione"):
        print (moltiplicazione (n1,n2))

    if (segno == "divisione"):
        if (n2 == 0):
            print ("impossibile")
        else:
            print (divisione (n1,n2))
    
    check = input("desideri continuare? Y/N")
    if (check == "Y"):
        continue
    if (check == "N"):
        break

    

    

    

