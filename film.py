from medias import Media

class Film(Media):
    def __init__(self, titre, genre, annee, realisateur, duree):
        super().__init__(titre, genre, annee)
        self._realisateur = realisateur
        self._duree = duree

    def afficher(self):
        return f"Film | {super().afficher()} | Réalisateur: {self._realisateur} | Durée: {self._duree} min"

    def to_dict(self):
        d = super().to_dict()
        d["_realisateur"] = self._realisateur
        d["_duree"] = self._duree
        return d
