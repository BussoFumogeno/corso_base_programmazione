i = 1
differenza = 0
ns = 33
while True:
    n = int(input("inserisci un numero: "))
    if (ns == n):
        break
        
    if (n > ns):
            print ("piu piccolo")
            differenza = n - ns
            if ( n < ns ):
                print ("piu grande")
                differenza = ns -n
    if (differenza>20):
        print ("acqua")
        
    if (10 < differenza):
        if(differenza < 20):
            print ("fuochino")
    
    if (10 > differenza ):
        print ("fuoco")

    
    i = i + 1
    
print (i)
print ("hai indovinato congratulazioni")

