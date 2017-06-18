import ctypes
from pygame import mixer


class ST:
    def __init__(self):
        mixer.init()

    def __del__(self):
        mixer.quit()


    def loadsound(self, sound: str, histoire: str, repeat: ctypes.c_int16):
        s = mixer.Sound("Musique/" + histoire + "/" + sound + ".ogg")
        r = repeat
        p = False

        return [s, r, p]

    def playsound(self, sound: mixer.Sound, repeat: ctypes.c_int16):
        mixer.Sound.play(sound, repeat)

    def stopsound(self, sound: mixer.Sound):
        mixer.Sound.stop(sound)


st = ST()