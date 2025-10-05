from medias import Media

class Livre(Media):
    def __init__(self, titre, genre, annee, auteur, pages):
        super().__init__(titre, genre, annee)
        self._auteur = auteur
        self._pages = pages

    def afficher(self):
        return f"Livre | {super().afficher()} | Auteur: {self._auteur} | Pages: {self._pages}"

    def to_dict(self):
        d = super().to_dict()
        d["_auteur"] = self._auteur
        d["_pages"] = self._pages
        return d
