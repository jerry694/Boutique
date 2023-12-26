
from menuPrincipal import *


if __name__ == "__main__":
    while True:
        afficher_menu()
        choix = int(input("Entrez votre choix : "))
        executer_action(choix)
        if choix == 6:
            break

