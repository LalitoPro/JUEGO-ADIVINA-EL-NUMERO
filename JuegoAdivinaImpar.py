from random import randrange
from JuegoAdivinaNumero import *

class JuegoAdivinaImpar(JuegoAdivinaNumero):

    def ValidaNumero(self, num):
        if num % 2 != 0:
            return True
        else:
            return False