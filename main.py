
from menuPrincipal import *


if __name__ == "__main__":
    while True:
        afficher_menu()
        choix = int(input("Entrez votre choix : "))
        executer_action(choix)
        if choix == 5:
            break


#
# for article in articles:
#     article.afficher_info()
#
# # Création d'une instance de la boutique
# ma_boutique = Boutique(articles)
#
# # Exemples d'utilisation des fonctions
# achats = {1: 3, 4: 2, 7: 1}  # Dictionnaire où la clé est l'identifiant de l'article et la valeur est la quantité achetée
#
# for identifiant, quantite in achats.items():
#     print(ma_boutique.vendre(identifiant, quantite))
#
# print(ma_boutique.consulter(1))  # Consultation du stock du premier article
#
# print(ma_boutique.approvisionner(1, 5))  # Approvisionnement du premier article
#
# print(ma_boutique.facture_total_achats(achats))  # Génération de la facture pour le total des achats
