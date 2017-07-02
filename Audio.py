from pygame import mixer
import Histoire
from Util import *


# Une classe pour gérer les sons
class ST:
    def __init__(self):
        mixer.init()
        log("Gestion de l'audio assuree !")

    def __del__(self):
        mixer.quit()


    def loadsound(self, sound: str, loop: bool):
        s = mixer.Sound("Aventures/" + Histoire.histoire + "/" + sound)
        r = loop
        p = False

        return [s, r, p]

    def playsound(self, sound: mixer.Sound, loop: bool):
        if not loop:
            sound.play(0)
        else:
            sound.play(-1)

    def stopsound(self, sound: mixer.Sound):
        sound.stop()


st = ST()