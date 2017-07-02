import pygame
import json
from Audio import st
from Util import *


# Classe Page, une fonction permettant de les charger à partir de fichiers .json, une exception, et deux variables indiquant l'histoire et la page actuelles
histoire = "Test"


class Page:
    def __init__(self, desc: description, actions: action, image: pygame.Surface, infoSon: son):
        self.desc = desc
        self.image = image
        self.son = infoSon
        self.actions = actions
        # Variable très moche pour quelques maths
        self._actMaths = len(self.actions) + 1

class LoadError(Exception):
    def __init__(self):
        Exception.__init__(self, "Page couldn't be loaded.")


def chargerpage(fichier: str):
    global histoire
    data = json.load(open("Aventures/" + histoire + "/" + fichier + ".json"))

    d = (data["desc"], pygame.Color(data["color"]))

    act = []
    for a in data["actions"]:
        act.append(Action((a["desc"], pygame.Color(a["color"])),
                          (a["cible"], a.get("histoire", histoire))))

    try:
        i = pygame.image.load_extended("Aventures/" + histoire + "/" + data["image"])
    except:
        i = None

    try:
        s = st.loadsound(data["son"], data["loop_music"])
    except:
        s = None

    return Page(d, act, i, s)


page = chargerpage("intro")