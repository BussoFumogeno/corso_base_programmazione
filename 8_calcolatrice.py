a = int(input("inserisci numero: "))
b = int(input("inserisci numero: "))
segno = int(input("inserisci il segno: "))

if (segno==1):
    print (a+b)

if (segno==2):
    print (a-b)

if (segno==3):
    if (b==0):
        print ("errore")
    else: 
        print(a/b)

if (segno==4):
    print (a*b)

if (segno==5):
    print (a+b)