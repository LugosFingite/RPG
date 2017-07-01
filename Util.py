#!/usr/bin/env python3

from pygame.mixer import Sound
from pygame import Color
import typing


log = lambda e: print("LOG:", e)

description = typing.Tuple[str, Color]

son = typing.Tuple[Sound, int, bool]


class Action:
    def __init__(self, desc: description, cible: str):
        self.desc = desc
        self.cible = cible

action = typing.List[Action]
