import time


def narra(testo, velocita=0.03):
    for carattere in testo:
        print(carattere, end="", flush=True)
        time.sleep(velocita)
    print()

def pausa():
    input("---Premi invio per continuare--- ")