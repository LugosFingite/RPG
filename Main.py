#!/usr/bin/env python3


import pygame
from Util import *
import Histoire
from UI import ui, _ui, _noImage
from Audio import st


# Notre jeu, dans une classe
class Game:
    # Quatre fonctions servant au bon fonctionnement du jeu
    def __init__(self):
        self.done = False
        log("Jeu chargé et prêt à jouer !")

    def run(self):
        try:
            ui.MAIN.blit(_ui, (0, 0))
            self.processpage(Histoire.page)
        except KeyError:
            raise Histoire.LoadError()

        self.events()
        self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def update(self):
        ui.update(16)

    # Une fonction qui transforme les données récupérées dans les fichiers .json en une page utilisable par l'utilisateur
    def processpage(self, p: Histoire.Page):
        if p.image != None:
            ui.MAIN.blit(p.image, (0, 0))
        else:
            ui.MAIN.blit(_noImage, (0, 0))

        if p.son != None and not p.son[2]:
            st.playsound(p.son[0], p.son[1])
            p.son[2] = True

        ui.cout(p.desc[0], p.desc[1])

        act = -1
        for a in range(ui.buttonZone[0], ui.buttonZone[0] + ui.buttonZone[1], ui.buttonZone[1] // p._actMaths):
            if act >= 0 and act < p._actMaths - 1:
                ui.button(a, p.actions[act])

            act += 1



rpg = Game()

while not rpg.done:
    rpg.run()
log("Projet terminé sans problèmes !")
