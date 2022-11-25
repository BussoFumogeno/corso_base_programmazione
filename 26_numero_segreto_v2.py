i = 0
numero_segreto = 7
while True:
    n = int(input("indovina il numero segreto: "))
    if (n - numero_segreto >= 20):
        print("acqua")

    if (n - numero_segreto > 10 ):
        if (n - numero_segreto < 20):
            print ("fuochino")

    if (n - numero_segreto <= 10):
        print("fuoco")
    
    i = i + 1
    
    if (n == numero_segreto):   
       break

    

print (i)


