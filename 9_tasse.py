guadagno = int(input("inserisci il tuo guadagno: "))
if (guadagno < 10000):
    print("paghi 0€")

if (guadagno >= 10000 and guadagno <= 30000):
    print(22/100*guadagno)

if (guadagno > 30000):
    print(22/100*20000+33/100*(guadagno-30000))