def scegli(*opzioni):
    print()

    for numero, opzione in enumerate(opzioni, start=1):
        print(f"{numero}. {opzione}")

    while True:
        risposta = input("> ").strip()

        if risposta.isdigit():
            scelta = int(risposta)

            if 1 <= scelta <= len(opzioni):
                return scelta

        print("Scelta non valida.")