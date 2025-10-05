class Bibliotheque:
    def __init__(self):
        self.medias = []

    def ajouter_media(self, media):
        self.medias.append(media)

    def get_tous(self):
        return self.medias

    def rechercher(self, titre):
        return [m for m in self.medias if titre.lower() in m.get_titre().lower()]

    def supprimer_media(self, titre):
        self.medias = [m for m in self.medias if m.get_titre().lower() != titre.lower()]
