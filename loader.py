import json
import glob
from typing import List


class Action:
    def __init__(self, desc: str, cible: str):
        self.desc = desc
        self.cible = cible


Actions = List[Action]


class Page:
    def __init__(self, id: str, image: str, son: str, desc: str, actions: Actions):
        self.id = id
        self.image = image
        self.son = son
        self.desc = desc
        self.actions = actions


def chargerPage(fichier: str):
    data = json.load(open(fichier))
    id = data["page"]
    image = data["image"]
    son = data["son"]
    desc = data["desc"]
    actions = []
    for action in data["actions"]:
        actions.append(action)

    page = Page(id, image, son, desc, actions)

    return page


def chargerAventure(dossier: str):
    pages = []
    for fichier in glob.iglob('**/*.json', recursive=True):
        pages.append(chargerPage(fichier))

    return pages
