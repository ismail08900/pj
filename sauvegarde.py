import json
from livre import Livre
from film import Film
from musique import Musique

FICHIER = "data.json"

def sauvegarder(medias):
    liste_a_sauvegarder = []
    for media in medias:
        d = media.__dict__.copy()
        d["__class__"] = media.__class__.__name__
        liste_a_sauvegarder.append(d)
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(liste_a_sauvegarder, f, ensure_ascii=False, indent=4)

def charger():
    try:
        with open(FICHIER, "r", encoding="utf-8") as f:
            liste_chargee = json.load(f)
        medias = []
        for d in liste_chargee:
            cls = d.pop("__class__", None)
            if cls == "Livre":
                media = Livre(**d)
            elif cls == "Film":
                media = Film(**d)
            elif cls == "Musique":
                media = Musique(**d)
            else:
                continue
            medias.append(media)
        return medias
    except (FileNotFoundError, json.JSONDecodeError):
        return []
