from game.dialogue import narra, pausa
from game.choices import scegli


def risveglio(game):
    narra("Ti svegli in un prato pieno di fiori rosso-sangue")
    narra("Non sai perchè sei lì")
    narra("Il sole è alto nel cielo ")
    pausa()
    narra("Ti guardi attorno e vedi solo una foresta che circonda il prato")

SCENE = {
    "risveglio": risveglio
}