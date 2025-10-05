class Media:
    def __init__(self, titre, genre, annee):
        self.titre = titre
        self.genre = genre
        self.annee = annee

    def afficher(self):
        return f"{self.titre} | {self.genre} | {self.annee}"

    def get_titre(self):
        return self.titre

    def to_dict(self):
        return {
            "titre": self.titre,
            "genre": self.genre,
            "annee": self.annee
        }
