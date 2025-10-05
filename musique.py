from medias import Media

class Musique(Media):
    def __init__(self, titre, genre, annee, artiste, duree):
        super().__init__(titre, genre, annee)
        self._artiste = artiste
        self._duree = duree

    def afficher(self):
        return f"Musique | {super().afficher()} | Artiste: {self._artiste} | Durée: {self._duree} min"

    def to_dict(self):
        d = super().to_dict()
        d["_artiste"] = self._artiste
        d["_duree"] = self._duree
        return d
