import pygame
from UI import ui
from Util import *


class Game:
    def __init__(self):
        self.done = False

    def run(self):
        ui.MAIN.fill(colors[0])
        ui.button("FuckU", 500, True)

        self.events()
        self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type != pygame.ACTIVEEVENT and event.type != pygame.MOUSEMOTION:
                log(event)

            if event.type == pygame.QUIT:
                self.done = True

    def update(self):
        ui.update(24)


rpg = Game()

while not rpg.done:
    rpg.run()