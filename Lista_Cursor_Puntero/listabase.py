from tipos import *
from nodo import *


class ListaBase:
    def __init__(self, TipoClave:TipoDatosClave, alSize:int):
        '''Crea una lista vacia'''
        self.q_items = 0
        self.TipoDeDato = TipoClave
        self.Size = alSize

    def EsVacia(self) -> bool:
        '''Control de una lista vacia'''
        return self.q_items == 0

    def EsLlena(self) -> bool:
        '''Control de una lista llena'''
        return self.q_items == self.Size

    def CantidadElementos(self) -> int:
        return self.q_items

    def DatoDeLaClave(self) -> TipoDatosClave:
        return self.TipoDeDato

    def SizeList(self) -> int:
        return self.Size