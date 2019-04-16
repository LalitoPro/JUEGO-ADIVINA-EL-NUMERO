from random import *
from JuegoAdivinaNumero import *
from JuegoAdivinaPar import *
from JuegoAdivinaImpar import *

s = int(input('Seleccione el tipo de Juego: \n 1 = Adivina Número \n 2 = Adivina Número Par \n 3 = Adivina Número Impar \n'))

if s == 1:

    juega = JuegoAdivinaNumero(randrange(10), 3)
    juega.Juega()
    while True:
        r = input('¿Quieres volver a intentar Si o No?')

        if r == "S":
            juega.ReiniciaPartida()
        else:
            print("\n Gracias por jugar :)")
            break

if s == 2:

    juega = JuegoAdivinaPar(choice([0, 2, 4, 6, 8, 10]), 3)
    juega.Juega()
    while True:
        r = input('¿Quieres volver a intentar?')

        if r == "S":
            juega.ReiniciaPartida()
        else:
            print("\n Gracias por jugar :)")
            break

if s == 3:
    juega = JuegoAdivinaPar(choice([1, 3, 5, 7, 9]), 3)
    juega.Juega()
    while True:
        r = input('¿Quieres volver a intentar?')

        if r == "S":
            juega.ReiniciaPartida()
        else:
             print("\n Gracias por jugar :)")
             break