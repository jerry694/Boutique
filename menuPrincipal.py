from boutique import *

# Création d'articles
article1 = Article(1, "Livre", 15.99, 20, 5)
article2 = Article(2, "Ordinateur portable", 899.99, 10, 2)
article3 = Article(3, "Télévision", 499.99, 15, 3)
article4 = Article(4, "Smartphone", 599.99, 25, 8)
article5 = Article(5, "Casque audio", 79.99, 30, 10)
article6 = Article(6, "Console de jeu", 299.99, 12, 4)
article7 = Article(7, "Cafetière", 39.99, 50, 15)
article8 = Article(8, "Chaussures de sport", 79.99, 40, 12)
article9 = Article(9, "Sac à dos", 29.99, 18, 6)
article10 = Article(10, "Enceinte Bluetooth", 49.99, 22, 7)

# Affichage des informations des articles
articles = [article1, article2, article3, article4, article5, article6, article7, article8, article9, article10]

# Création d'une instance de la boutique
ma_boutique = Boutique(articles)


def afficher_menu():
    print("1. Vendre un article")
    print("2. Approvisionner un article")
    print("3. Consulter le stock d'un article")
    print("4. Générer la facture totale des achats")
    print("5. Details sur un article")
    print("6. Quitter")

def executer_action(choix):
    if choix == 1:
        ma_boutique.liste()
        identifiant = int(input("Entrez l'identifiant de l'article à vendre : "))
        quantite = int(input("Entrez la quantité à vendre : "))
        print(ma_boutique.vendre(identifiant, quantite))
    elif choix == 2:
        ma_boutique.liste()
        identifiant = int(input("Entrez l'identifiant de l'article à approvisionner : "))
        quantite = int(input("Entrez la quantité à approvisionner : "))
        print(ma_boutique.approvisionner(identifiant, quantite))
    elif choix == 3:
        ma_boutique.liste()
        identifiant = int(input("Entrez l'identifiant de l'article à consulter : "))
        print(ma_boutique.consulter(identifiant))
    elif choix == 4:

        print(ma_boutique.facture_total_achats())
    elif choix == 6:
        print("Merci et au revoir !")
    elif choix == 5:
        ma_boutique.liste()
        print("\n \n")
        identifiant = int(input("Entrez l'identifiant de l'article à detailler : "))
        print(ma_boutique.detailsArticle(identifiant))

    else:
        print("Choix invalide.")


