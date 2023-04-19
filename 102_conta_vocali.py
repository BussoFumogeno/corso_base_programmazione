numero_vocali=0
i = 0
frase = str(input("inserisci una frase: "))
lung_frase=len (frase)
while (i < lung_frase):
    if (frase [i] == "a" or frase [i] == "e" or frase [i] == "i" or frase [i] == "o" or frase [i] == "u" or frase [i] == "A" or frase [i] == "E" or frase [i] == "I" or frase [i] == "O" or frase [i] == "U" ):

        numero_vocali = numero_vocali + 1
    i = i + 1
print (numero_vocali)



