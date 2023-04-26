#Chiedi una stringa all'utente. Stampa la stringa inserita senza le vocali.
consonanti=""
i = 0
frase = str(input("inserisci una frase: "))
lung_frase=len (frase)
while (i < lung_frase):
    if (frase [i]!= "a" and frase [i] != "e" and frase [i] != "i" and frase [i] != "o" and frase [i] != "u" and frase [i] != "A" and frase [i] != "E" and frase [i] != "I" and frase [i] != "O" and frase [i] != "U" ):

        consonanti = consonanti + frase[i]
    i = i + 1
print (consonanti)