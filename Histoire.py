#!/usr/bin/env python3

import pygame
import json, glob
from Audio import st
from Util import *


class Page:
    def __init__(self, desc: description, actions: action, image: pygame.Surface, infoSon: son):
        self.desc = desc
        self.image = image
        self.son = infoSon
        self.actions = actions
        self._actMaths = len(self.actions) + 1


def chargerpage(fichier: str):
    data = json.load(open(fichier))

    d = (data["desc"], pygame.Color(data.get("textColor", "white")))
    act = []
    for a in data["actions"]:
        act.append(Action((a["desc"], pygame.Color(a.get("textColor", "white"))), a["cible"]))

    try:
        i = pygame.image.load_extended("Graphismes\\Histoires\\" + data["image"] + ".png")
    except:
        i = None

    try:
        s = st.loadsound(data["son"], data["son.repeat"])
    except:
        s = None

    return Page(d, act, i, s)

def chargerhistoire():
    pages = {}
    for p in glob.iglob("Aventures\\*\\**.json", recursive = True):
        pages[p] = chargerpage(p)

    return pages


page = "Aventures\\Test\\intro.json"
pages = chargerhistoire()
