conta_vocali1=0
conta_vocali2=0
i=0
while True:
    stringa1=input("inserisci una stringa: ").lower()
    stringa2=input("inserisci una stringa: ").lower()
    l1= len(stringa1)
    l2= len(stringa2)
    if (stringa1[i]=="a" or stringa1[i]=="e" or stringa1[i]=="i" or stringa1[i]=="o" or stringa1[i]=="u"):
        conta_vocali1=conta_vocali1 + 1
    if (stringa2[i]=="a" or stringa2[i]=="e" or stringa2[i]=="i" or stringa2[i]=="o" or stringa2[i]=="u"):
        conta_vocali2=conta_vocali2 + 1
    if ( conta_vocali1!= conta_vocali2):
        stringa1=input("inserisci una stringa: ").lower()
        stringa2=input("inserisci una stringa: ").lower()
        l1= len(stringa1)
        l2= len(stringa2)
    else:
        if (l1==l2):
            break
