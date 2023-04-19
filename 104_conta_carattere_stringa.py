#Chiedere all'utente una stringa ed un carattere. Contare quante volte quel carattere è presente nella stringa.
i = 0
numero_caratteri = 0
frase = input("inserisci una frase: ")
carattere = input("inserisci un carattere: ")
lung= len(frase)
while (i < lung):
    if (frase [i] == carattere):

        numero_caratteri = numero_caratteri + 1
    i = i + 1
print (numero_caratteri)