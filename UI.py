import pygame
import ctypes
from Util import *


_MAXCHAR = 72
_IGNORE = [' ', '.', ',', '!', '?', ':', ';']

_icon = pygame.image.load_extended("Graphism\\Icon.png")
_button1 = pygame.image.load_extended("Graphism\\Button1.png")
_button2 = pygame.image.load_extended("Graphism\\Button2.png")


class UI:
    def __init__(self, name : str):
        pygame.init()

        self.res = (600, 800)

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

    def _write(self, text: str, color: tuple, size : ctypes.c_int16, x: ctypes.c_int16, y: ctypes.c_int16, center: bool = False):
        visual = pygame.font.SysFont("Candara", size)
        surface = visual.render(text, True, color)

        if not center:
            rectangle = surface.get_rect(x = x, y = y)
        else:
            rectangle = surface.get_rect(centerx = x, centery = y)

        self.MAIN.blit(surface, rectangle)

    def cout(self, text: str, color: tuple, y: ctypes.c_int16):
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

            temp.append(char)

            prevChar = char
        lines.append("".join(temp))
        temp.clear()

        line = 0
        for show in lines:
            self._write(show, color, 16, 20, y + line)
            line += 16

        return len(lines)

    def button(self, text : str, y: ctypes.c_int16, action, textColor : tuple = colors[1]):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 40 < mouse[0] < self.res[0] - 40 and y < mouse[1] < y + 24:
            self.MAIN.blit(_button2, (40, y))

            if click[0] == 1:
                try:
                    action()
                except:
                    log("Le paramètre \"action\" n'est pas une fonction.")
        else:
            self.MAIN.blit(_button1, (40, y))

        self._write(text, textColor, 20, self.res[0] // 2, y + 13, center = True)


ui = UI("RPG")