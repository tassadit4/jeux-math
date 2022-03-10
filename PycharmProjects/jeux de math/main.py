import random
nb_min =1
nb_max=10

def resultat():

    A = random.randint(nb_min, nb_max)
    B = random.randint(nb_min, nb_max)
    O =random.randint(0, 1)
    cal = "+"
    if O == 1:
        cal ="*"
    resultat = 0
    while resultat == 0:
        resultat = (input(f"{A} {cal} {B}="))
        try:
            resultat = int(resultat)
        except:
            print("erreur: rentrer un nombre")
            resultat = 0
    C = resultat
    R = A + B
    if O == 1:
        R = A * B

    if C == R:
        return True

    return False


def poser_plusier_question():
    n=4
    vies=0

    for i in range (0, n):
        print("")
        print(f"Question n°{i + 1} sur {n}")
        C = resultat()
        if C == True:
                print('resultat est correcte')
                vies = vies + 1
                print(f"votre score est {vies}")
        else:
             print("resultat est faux")
             print(f"votre score est {vies}")

    print("")
    print(f"score finale est {vies}/ {n}")

    moyenne = (n/2)
    M = int(moyenne)
    if vies == n:
        print ('excellent vous aver réussi le teste')
    elif  vies == 0:
        print("réviser vous math")
    elif vies == M:
        print("vous etes moyen")
    elif M < vies:
        print("vous pouver faire mieux")
    else:
        print("vous etes faible")
poser_plusier_question()

