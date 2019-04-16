import abc
from abc import ABC
from random import *

class Juego(ABC):

    _num = int(0)
    _numVidas = int(0)
    _intentos = int(0)

    @abc.abstractmethod
    def Juega(self):
        return 0

    def QuitaVida(self):
        self._numVidas = self._numVidas - 1
        if self._numVidas > 0:
            return True
        else:
            return False

    def ReiniciaPartida(self):
        self._numVidas = 3
        self._num = randrange(10)
        self._intentos = 0
        self.Juega()

    def ActualizaRecord(self):
        self._intentos = self._intentos + 1