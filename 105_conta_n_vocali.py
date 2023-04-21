#Conta il numero di vocali e stampane il risultato per ogni vocale. Giorgio. a=0, e=0, i=2, o=2, u=0
conta_a=0
conta_e=0
conta_i=0
conta_o=0
conta_u=0
i=0
frase = input("inserisci una frase: ")
lung=len(frase)
while (i < lung):
    if (frase [i] == "a" or frase [i] == "A"):
        conta_a = conta_a + 1
    if (frase [i] == "e" or frase [i] == "E"):
        conta_e = conta_e + 1
    if (frase [i] == "i" or frase [i] == "I"):
        conta_i = conta_i + 1
    if (frase [i] == "o" or frase [i] == "O"):
        conta_o = conta_o + 1
    if (frase [i] == "u" or frase [i] == "U"):
        conta_u = conta_u + 1
    i = i + 1

print("a=" + str(conta_a))
print ("e=" + str(conta_e))
print ("i=" +str(conta_i))
print ("o=" + str (conta_o))
print ("u=" + str(conta_u))