from random import *
from Juego import *

class JuegoAdivinaNumero(Juego):

    def __init__(self, num, numVidas):

        self._num = num
        self._numVidas = numVidas

        if (num < 0 and numVidas < 0):
            self._num = 0
            self._numVidas = 0

    def Juega(self):

        while self._numVidas:
            print('Numero de vidas:', self._numVidas)
            #print('Numero que adivinar:', self._num)
            num = int(input('\n Intruduce el numero a adivinar: '))

            #print('Numero:', num)

            if (num == self._num):
                self.ActualizaRecord()
                print('\n Acertaste!!, En el intento:', self._intentos, ', El numero era:', self._num)
                break
            else:
                self.ActualizaRecord()
                if self.QuitaVida():
                    if (num > self._num):
                        print('Lo siento vuelvelo a intentar el numero es menor a', num)
                    if (num < self._num):
                        print('Lo siento vuelvelo a intentar el numero es mayor a', num)

                else:
                    print('Lo siento has perdido, el número era ', self._num)

    def ValidaNumero(self, num):
        self._num = num
        return True
