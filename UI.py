import pygame


class UI:
    def __init__(self, width : int, height : int, name : str, icon : pygame.Surface):
        pygame.init()

        self.res = (width, height)

        self.MAIN = pygame.display.set_mode(self.res)
        self.NAME = pygame.display.set_caption(name)
        self.ICON = pygame.display.set_icon(icon)
        self.CLOCK = pygame.time.Clock()

    def update(self, fps : int):
        pygame.display.update()
        self.CLOCK.tick(fps)


_icon = pygame.image.load_extended("Icon.png")

ui = UI(600, 800, "RPG", _icon)