somma_num=0
lettere = 0
i = 0
while( lettere == 0 ):
    frase = input("inserisci una frase di soli numeri: ")
    lung_frase = len (frase)
    while (i < lung_frase):
        if ( frase [i] == "1" or frase [i] == "2" or frase [i] == "3" or frase [i] == "4" or frase [i] == "5" or frase [i] == "6" or frase [i] == "7" or frase [i] == "8" or frase [i] == "9" or frase [i] == "0"):
            somma_num = somma_num + int(frase [i])
            
            lettere =  1
        else:
            lettere = 0
            break
        i = i + 1
print(somma_num)
    
    

