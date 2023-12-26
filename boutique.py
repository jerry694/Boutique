class Article:
    def __init__(self, identifiant, nom, prix_unitaire, stock_disponible, stock_limite):
        self.identifiant = identifiant
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.stock_disponible = stock_disponible
        self.stock_limite = stock_limite

    def afficher_info(self):
        print(f"Article: {self.nom} (ID: {self.identifiant})")
        print(f"Prix unitaire: {self.prix_unitaire * 655} Fcfa")
        print(f"Stock disponible: {self.stock_disponible}")
        print(f"Stock limite: {self.stock_limite}")
        print("\n")

    def simple_info(self):
        print(f"Article: {self.nom} (ID: {self.identifiant})")



class Boutique:
    def __init__(self, articles, achats = {}):
        self.articles = articles
        self.achats = achats

    def vendre(self, identifiant, quantite):
        for article in self.articles:
            if article.identifiant == identifiant:
                if quantite <= article.stock_disponible:
                    article.stock_disponible -= quantite
                    self.achats[identifiant]=quantite
                    print(self.achats)
                    return f"{quantite} {article.nom}(s) vendu(s)."
                else:
                    return f"Stock insuffisant pour {article.nom}."
        return "Article non trouvé."

    def approvisionner(self, identifiant, quantite):
        for article in self.articles:
            if article.identifiant == identifiant:
                article.stock_disponible += quantite
                return f"{quantite} {article.nom}(s) approvisionné(s)."
        return "Article non trouvé."

    def liste(self):
        for article in self.articles:
            article.simple_info()

    def detailsArticle(self, identifiant):
        for article in self.articles:
            if article.identifiant == identifiant:
                print(article.afficher_info())
    def consulter(self, identifiant):
        for article in self.articles:
            if article.identifiant == identifiant:
                return f"Stock disponible de {article.nom}: {article.stock_disponible}"
        return "Article non trouvé."

    def trouverArticle(self, identifiant):
        for article in self.articles:
            if article.identifiant == identifiant:
                return article

    def facture_total_achats(self):
        total = 0
        print(
            "____________________________________________________________________________________________________________")

        print("ID\t\tNom\t\tPrixUnitaire\t\tQuantite\t\tPrixTotal")
        for identifiant, quantite in self.achats.items():
            # print(f"Identifiant de l'article : {identifiant}, Quantité achetée : {quantite}")
            article = self.trouverArticle(identifiant)
            total = total + article.prix_unitaire*quantite
            # print(article.prix_unitaire)
            print(f"{article.identifiant}\t\t{article.nom}\t\t{article.prix_unitaire*655}Fcfa\t\t{quantite}\t\t{article.prix_unitaire*quantite*655}Fcfa")
            print("----------------------------------------------------------------------------------------------------------")

        print(f"\n \t\t {article.prix_unitaire*quantite*655}Fcfa")
        print(
            "____________________________________________________________________________________________________________")
        self.achats = {}