#Chiedi all'utente 2 stringhe. Controlla che tutti i caratteri presenti nella prima stringa siano presenti nella seconda striga. 
#Non importa la posizione. 
#Stampa il risultato se vero o falso.
I=0
i=0
frase1 = input("inserisci una frase: ")
frase2 = input("inserisci una frase: ")
lung1 = len(frase1)
while (i < lung1):
    if (frase1[i] in frase2):
        i = i + 1
        print ("vero")
    else:
        print("falso")
        break
        
        