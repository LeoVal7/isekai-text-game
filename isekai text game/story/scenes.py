from game.dialogue import narra, pausa
from game.choices import scegli


def risveglio(game):
    narra("Ti svegli in un prato pieno di fiori rosso-sangue")
    narra("Non sai perchè sei lì")
    narra("Il sole è alto nel cielo ")
    pausa()
    narra("Ti guardi attorno e vedi solo una foresta che circonda il prato")
    scelta = scegli(
        "Osserva il prato",
        "Guardare verso la foresta",
        "Prova a ricordare come sei arrivato qui"
    )
    if scelta == 1:
        narra("Il prato è pieno di fiori rossi e il vento li fa ondeggiare dolcemente")
        pausa()
        return "risveglio"
    elif scelta == 2:
        narra("La foresta sembra oscura e minacciosa, ma c'è un sentiero che porta verso di essa")
        pausa()
        return "risveglio"
    elif scelta == 3:
        narra("Non ricordi nulla, solo un senso di vuoto e confusione")
        pausa()
        return "risveglio"
SCENE = {
    "risveglio": risveglio
}