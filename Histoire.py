import pygame
import json, glob
from Audio import st
from Util import *

import sys


class Page:
    def __init__(self, desc: description, actions: action, image: pygame.Surface, infoSon: son):
        self.desc = desc
        self.image = image
        self.son = infoSon
        self.actions = actions
        self._actMaths = len(self.actions) + 1


def chargerpage(fichier: str, histoire: str):
    data = json.load(open(fichier))

    d = (data["desc"], pygame.Color(data.get("textColor", "white")))
    act = []
    for a in data["actions"]:
        act.append(Action((a["desc"], pygame.Color(a.get("textColor", "white"))), a["cible"]))

    try:
        print("Graphismes/Histoires/" + histoire + "/" + data["image"] + ".png")
        i = pygame.image.load_extended("Graphismes/Histoires/" + histoire + "/" + data["image"] + ".png")
    except:
        i = None

    try:
        s = st.loadsound(data["son"], histoire, data["son.repeat"])
    except:
        s = None

    return Page(d, act, i, s)

def chargerhistoire(histoire: str):
    pages = {}
    for p in glob.iglob("Aventures/" + histoire + "/**.json", recursive = True):
        pages[p] = chargerpage(p, histoire)

    return pages


page = "Aventures/" + sys.argv[1] + "/intro.json"
pages = chargerhistoire(sys.argv[1])