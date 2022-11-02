B = 10
C = 0

while C <= B:
    As = input("indovina il numero magico: ")
    A = int(As)

    
    if (A == 7):
        print("Complimenti, hai indovinato!")
        break
    else:
        C = C + 1

    if (C > 10):
        print("Game over!")


