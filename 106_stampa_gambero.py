#Inserisci una parola/frase. Stampa il risultato partendo da destra. Es. Giorgio diventa "oigroiG"
frase = input("inserisci una frase: ")
i = len(frase)-1
lettera = ""
while (i >= 0):
    lettera = lettera + frase[i]
    i=i-1
print (lettera)