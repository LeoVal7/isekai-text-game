from game.player import Player
from story.scenes import SCENE


class Game:
    def __init__(self):
        self.player = Player()
        self.stato = {}

    def start(self):
        scena_corrente = "prato"

        while scena_corrente is not None:
            scena = SCENE.get(scena_corrente)

            if scena is None:
                print(f"Errore: scena '{scena_corrente}' non trovata.")
                break

            scena_corrente = scena(self)