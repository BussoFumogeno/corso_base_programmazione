import random
carta1_dealer = 0
carta2_dealer = 0
carta3_dealer = 0
carta4_dealer = 0
carta1_sfidante = 0
carta2_sfidante = 0
carta3_sfidante = 0
carta4_sfidante = 0
carta5_sfidante = 0
decisione_giocatore = 0
punteggio = 0
punteggio_dealer = 0

while True:
    print ("le chips non devono essere maggiori di 100 o minori di 20")
    somma_puntata_dealer = random.randrange(20,100)
    somma_puntata = int(input("quante chips desideri puntare?: "))
    if (somma_puntata > 100):
        print ("la somma puntata è troppo grande")

    if (somma_puntata < 20):
        print ("la somma puntata è troppo piccola")

    if (somma_puntata >= 20):
        if (somma_puntata <= 100):
            print ("hai puntato la tua somma")
            break


carta_dealer = random.randrange(1,13)
carta1_sfidante = random.randrange(1,13)
carta2_sfidante = random.randrange(1,13)


print ("le carte dello sfidante sono: ")
print (carta1_sfidante)
if (carta1_sfidante == 11):
    print ("jack")
if (carta1_sfidante == 12):
    print ("donna")
if (carta1_sfidante == 13):
    print("re")
if (carta1_sfidante == 1):
    print("asso")

print (carta2_sfidante)
if (carta2_sfidante == 11):
    print ("jack")
if (carta2_sfidante == 12):
    print ("donna")
if (carta2_sfidante == 13):
    print("re")
if (carta2_sfidante == 1):
    print("asso")

print ("la carta del dealer è: ")
print (carta_dealer)
if (carta1_dealer == 11):
    print ("jack")
if (carta1_dealer == 12):
    print ("donna")
if (carta1_dealer == 13):
    print("re")
if (carta1_dealer == 1):
    print("asso")


if (carta1_sfidante == 1):
    punteggio = punteggio + 11
if (carta1_sfidante >= 2 and carta1_sfidante <=10):
    punteggio = punteggio + carta1_sfidante
if (carta1_sfidante >= 11 and carta1_sfidante <=13):
    punteggio = punteggio + 10


if (carta2_sfidante == 1):
    punteggio = punteggio + 11
if (carta2_sfidante >= 2 and carta2_sfidante <=10):
    punteggio = punteggio + carta2_sfidante
if (carta2_sfidante >= 11 and carta2_sfidante <=13):
    punteggio = punteggio + 10

print ("il tuo punteggio è: "+str(punteggio))

if (punteggio == 21):
    print ("hai vinto ")
    quit()



decisione_giocatore = int(input("se desideri chiedere carta digita 1, se desideri restare digita 0"))


if (decisione_giocatore == 1):   
    carta3_sfidante = random.randrange(1,13)
    print (carta3_sfidante)
    if (carta3_sfidante == 11):
        print ("jack")
    if (carta3_sfidante == 12):
        print ("donna")
    if (carta3_sfidante == 13):
        print("re")
    if (carta3_sfidante == 1):
        print("asso")

    if (carta3_sfidante == 1):
        punteggio = punteggio + 11
    if (carta3_sfidante >= 2 and carta3_sfidante <=10):
        punteggio = punteggio + carta3_sfidante
    if (carta3_sfidante >= 11 and carta3_sfidante <=13):
        punteggio = punteggio + 10

    print (punteggio)

if (punteggio == 21):
    print ("hai vinto " )
    quit()

if (punteggio > 21):
    print ("hai perso ")
    quit()


carta1_dealer = random.randrange(1,13)
if (carta1_dealer == 11):
    print ("jack")
if (carta1_dealer == 12):
    print ("donna")
if (carta1_dealer == 13):
    print("re")
if (carta1_dealer == 1):
    print("asso")

if (carta1_dealer == 1):
    punteggio_dealer = punteggio_dealer + 11
if (carta1_dealer >= 2 and carta1_dealer <=10):
    punteggio_dealer = punteggio_dealer + carta1_dealer
if (carta1_dealer >= 11 ):
    punteggio_dealer = punteggio_dealer + 10

carta2_dealer = random.randrange(1,13)
print ("la carta del dealer è: ")
print (carta2_dealer)
if (carta2_dealer == 11):
    print ("jack")
if (carta2_dealer == 12):
    print ("donna")
if (carta2_dealer == 13):
    print("re")
if (carta2_dealer == 1):
    print("asso")

if (carta2_dealer == 1):
    punteggio_dealer = punteggio_dealer + 11
if (carta2_dealer >= 2 and carta2_dealer <=10):
    punteggio_dealer = punteggio_dealer + carta2_dealer
if (carta2_dealer >= 11 ):
    punteggio_dealer = punteggio_dealer + 10


if (punteggio_dealer >= 17):
    if (punteggio_dealer > 21):
        print ("hai vinto")
        quit()
    if (punteggio_dealer == punteggio):
        print ("pareggio")

    if (punteggio_dealer > punteggio):
        print ("hai perso")

    if(punteggio_dealer < punteggio):
        print ("hai vinto")
    quit()


decisione_giocatore = int(input("se desideri chiedere carta digita 1, se desideri restare digita 0"))


if (decisione_giocatore == 1):
    carta4_sfidante = random.randrange(1,13)
    print (carta4_sfidante)
    if (carta4_sfidante == 11):
        print ("jack")
    if (carta4_sfidante == 12):
        print ("donna")
    if (carta4_sfidante == 13):
        print("re")
    if (carta4_sfidante == 1):
        print("asso")

    if (carta4_sfidante == 1):
        punteggio = punteggio + 11
    if (carta4_sfidante >= 2 and carta4_sfidante <=10):
        punteggio = punteggio + carta4_sfidante
    if (carta4_sfidante >= 11 and carta4_sfidante <=13):
        punteggio = punteggio + 10

    print (punteggio)

if (punteggio == 21):
    print ("hai vinto")
    quit()

if (punteggio > 21):
    print ("hai perso ")
    quit()


carta3_dealer = random.randrange(1,13)
print ("la carta del dealer è: ")
print (carta3_dealer)
if (carta3_dealer == 11):
    print ("jack")
if (carta3_dealer == 12):
    print ("donna")
if (carta3_dealer == 13):
    print("re")
if (carta3_dealer == 1):
    print("asso")

if (carta3_dealer == 1):
    punteggio_dealer = punteggio_dealer + 11
if (carta3_dealer >= 2 and carta3_dealer <=10):
    punteggio_dealer = punteggio_dealer + carta3_dealer
if (carta3_dealer >= 11 ):
    punteggio_dealer = punteggio_dealer + 10


if (punteggio_dealer >= 17):
    if (punteggio_dealer > 21):
        print ("hai vinto")
        quit()
    if (punteggio_dealer == punteggio):
        print ("pareggio")

    if (punteggio_dealer > punteggio):
        print ("hai perso")

    if(punteggio_dealer < punteggio):
        print ("hai vinto")
    quit()

decisione_giocatore = int(input("se desideri chiedere carta digita 1, se desideri restare digita 0"))


if (decisione_giocatore == 1):
    carta3_sfidante = random.randrange(1,13)
    print (carta5_sfidante)
    if (carta5_sfidante == 11):
        print ("jack")
    if (carta5_sfidante == 12):
        print ("donna")
    if (carta5_sfidante == 13):
        print("re")
    if (carta5_sfidante == 1):
        print("asso")

    if (carta5_sfidante == 1):
        punteggio = punteggio + 11
    if (carta5_sfidante >= 2 and carta5_sfidante <=10):
        punteggio = punteggio + carta5_sfidante
    if (carta5_sfidante >= 11 and carta5_sfidante <=13):
        punteggio = punteggio + 10

    print (punteggio)

if (punteggio == 21):
    print ("hai vinto")
    quit()

if (punteggio > 21):
    print ("hai perso ")
    quit()


carta4_dealer = random.randrange(1,13)
print ("la carta del dealer è: ")
print (carta4_dealer)
if (carta4_dealer == 11):
    print ("jack")
if (carta4_dealer == 12):
    print ("donna")
if (carta4_dealer == 13):
    print("re")
if (carta4_dealer == 1):
    print("asso")

if (carta4_dealer == 1):
    punteggio_dealer = punteggio_dealer + 11
if (carta4_dealer >= 2 and carta4_dealer <=10):
    punteggio_dealer = punteggio_dealer + carta4_dealer
if (carta4_dealer >= 11 ):
    punteggio_dealer = punteggio_dealer + 10


if (punteggio_dealer >= 17):
    if (punteggio_dealer > 21):
        print ("hai vinto")
        quit()
    if (punteggio_dealer == punteggio):
        print ("pareggio")

    if (punteggio_dealer > punteggio):
        print ("hai perso")

    if(punteggio_dealer < punteggio):
        print ("hai vinto")
    quit()


















