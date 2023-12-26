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

class Boutique:
    def __init__(self, articles):
        self.articles = articles

    def vendre(self, identifiant, quantite):
        for article in self.articles:
            if article.identifiant == identifiant:
                if quantite <= article.stock_disponible:
                    article.stock_disponible -= quantite
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

    def consulter(self, identifiant):
        for article in self.articles:
            if article.identifiant == identifiant:
                return f"Stock disponible de {article.nom}: {article.stock_disponible}"
        return "Article non trouvé."

    def facture_total_achats(self, achats):
        total = sum(achats.values())
        return f"Facture : Total des achats = {total*655} Fcfa."