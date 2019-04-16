from random import *
from JuegoAdivinaNumero import *

class JuegoAdivinaPar(JuegoAdivinaNumero):

    #def Juega(self):
     #   return 1

    def ValidaNumero(self, num):
        if num % 2 == 0:
            return True
        else:
            return False