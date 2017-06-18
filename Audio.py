import ctypes
from pygame import mixer
from Util import *


class ST:
    def __init__(self):
        mixer.init()
        log("Gestion de l'audio assurée !")

    def __del__(self):
        mixer.quit()


    def loadsound(self, sound: str, repeat: ctypes.c_int16):
        s = mixer.Sound("Musique\\" + sound + ".ogg")
        r = repeat
        p = False

        return [s, r, p]

    def playsound(self, sound: mixer.Sound, repeat: ctypes.c_int16):
        mixer.Sound.play(sound, repeat)

    def stopsound(self, sound: mixer.Sound):
        mixer.Sound.stop(sound)


st = ST()