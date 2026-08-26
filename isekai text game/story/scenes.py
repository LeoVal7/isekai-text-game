from game.dialogue import narra
from game.choices import scegli


def prato(game):
    narra("Ti trovi in un prato.")
    scelta = scegli(
        "Osserva il prato",
        "Avvicinati alla foresta",
        "Rimani qui",
    )

    if scelta == 1:
        narra("Non noti nulla di particolare.")
        return "prato"

    elif scelta == 2:
        return "foresta"

    elif scelta == 3:
        narra("Decidi di rimanere dove sei.")
        return "prato"


def foresta(game):
    narra("Ti trovi ai margini della foresta.")

    scelta = scegli(
        "Torna al prato",
        "Entra nella foresta"
    )

    if scelta == 1:
        return "prato"

    else:
        narra("Fai qualche passo tra gli alberi.")
        return "foresta"


SCENE = {
    "prato": prato,
    "foresta": foresta
}