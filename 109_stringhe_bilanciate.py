#Chiedi all'utente 2 stringhe. Controlla che tutti i caratteri presenti nella prima stringa siano presenti nella seconda striga e che i caratteri della seconda stringa siano presenti nella prima.
#non importa la posizione.
#Stampa il risultato se vero o falso.
stampa = 0
I=0
i=0
frase1 = input("inserisci una frase: ")
frase2 = input("inserisci una frase: ")
lung1 = len(frase1)
lung2 = len(frase2)
while (i < lung1):
    if (frase1[i] in frase2):
        i = i + 1
        stampa= ("vero")
    else:
        
        
    
        stampa= ("falso")
        break
if( stampa== "vero"):
    while (I < lung2):
        if (frase2[I] in frase1):
            I = I + 1
            stampa = ("vero")
        else:
            stampa = ("falso")
            break
print (stampa)