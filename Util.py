from pygame.mixer import Sound
from pygame import Color
import typing


log = lambda e: print("LOG:", e)

# Quelques types utiles
description = typing.Tuple[str, Color]
son = typing.Tuple[Sound, bool, bool]
cible = typing.Tuple[str, str]


class Action:
    def __init__(self, desc: description, pageCiblee):
        self.desc = desc
        self.cible = pageCiblee[0]
        self.histoireCiblee = pageCiblee[1]

action = typing.List[Action]