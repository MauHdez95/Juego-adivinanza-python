import random


def juego_adivinanza():
    # Generar un número aleatorio del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    # Primeras líneas del juego donde se da la bienvenida
    print("!Bienbenido al juego de adivinanza de número!")
    print("Debes adeivinar el número secreto que puede ser un valor entre 1 y 100")
    print("!Intenta adivinarlo!")

    while not adivinado:
        # Solicitar un número del 1 al 100
        adivinanza = input("Escoge un número entre el 1 y el 100 y escribelo:")

        # Verificar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(
                adivinanza
            )  # Lo estamos pasando de cadena (str) a número entero (int)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(
                    f"!Felicidades has ganado! El número {adivinanza} es el secreto y lo has logrado en {intentos} intentos"
                )
                break
        else:
            print("Por favor introduce un número entre el 1 y el 100")

juego_adivinanza()