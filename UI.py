#!/usr/bin/env python3

import pygame
import ctypes
from Audio import st
import Histoire
from Util import *


_MAXCHAR = 72
_IGNORE = [' ', '.', ',', '!', '?', ':', ';']

_icon = pygame.image.load_extended("Graphismes\\Icon.png")
_ui = pygame.image.load_extended("Graphismes\\UI.png")
_button1 = pygame.image.load_extended("Graphismes\\Button1.png")
_button2 = pygame.image.load_extended("Graphismes\\Button2.png")
_button3 = pygame.image.load_extended("Graphismes\\Button3.png")
_noImage = pygame.image.load_extended("Graphismes\\NoImage.png")


class UI:
    def __init__(self, name : str):
        pygame.init()

        self.res = (600, 800)
        self.buttonZone = (640, 150)

        self.MAIN = pygame.display.set_mode(self.res)
        self.NAME = pygame.display.set_caption(name)
        self.ICON = pygame.display.set_icon(_icon)
        self.CLOCK = pygame.time.Clock()

        log("Fenêtre créée !")

    def update(self, fps : int):
        pygame.display.update()
        self.CLOCK.tick(fps)

    def __del__(self):
        pygame.quit()


    def _write(self, text: str, textColor: pygame.Color, size : ctypes.c_int16, x: ctypes.c_int16, y: ctypes.c_int16, center: bool = False):
        visual = pygame.font.SysFont("Candara", size)
        surface = visual.render(text, True, textColor)

        if not center:
            rectangle = surface.get_rect(x = x, y = y)
        else:
            rectangle = surface.get_rect(centerx = x, centery = y)

        self.MAIN.blit(surface, rectangle)

    def cout(self, text: str, textColor: pygame.Color):
        text = list(text)
        lines = []
        temp = []
        prevChar = ' '

        for char in text:
            if len(temp) == _MAXCHAR or char == '\n':
                if (char in _IGNORE or prevChar in _IGNORE) and char != '\n':
                    temp.append(char)
                elif char != '\n':
                    temp.append('-')

                lines.append("".join(temp))
                temp.clear()

            if char != '\n':
                temp.append(char)

            prevChar = char
        lines.append("".join(temp))
        temp.clear()

        line = 0
        for show in lines:
            self._write(show, textColor, 16, 20, 302 + line)
            line += 16

        return len(lines)

    def button(self, y: ctypes.c_int16, action : Action):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 40 < mouse[0] < self.res[0] - 40 and y < mouse[1] < y + 24:
            if click[0] == 0:
                self.MAIN.blit(_button2, (40, y))
            elif click[0] == 1:
                self.MAIN.blit(_button3, (40, y))

                if Histoire.pages[Histoire.page].son != None:
                    st.stopsound(Histoire.pages[Histoire.page].son[0])
                    Histoire.pages[Histoire.page].son[2] = False
                Histoire.page = "Aventures\\" + action.cible + ".json"

        else:
            self.MAIN.blit(_button1, (40, y))

        self._write(action.desc[0], action.desc[1], 20, self.res[0] // 2, y + 13, center = True)


ui = UI("RPG")
