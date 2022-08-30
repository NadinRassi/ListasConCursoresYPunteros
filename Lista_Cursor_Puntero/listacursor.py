from unittest import result
from tipos import *
from nodo import *
from listabase import * 

MIN = 1
MAX = 2000
NULO = 0

PosicionLista = int


class Lista(ListaBase): #lista base es el padre

    def __init__(self, TipoClave:TipoDatosClave, alSize:int):
        '''Crea una lista vacia'''
        if MIN <= alSize <= MAX:
            self.cursor = []
            for Q in range(alSize+1): #la posicion 0 no la usamos pero la tenemos en cuenta
                nodo = Nodo()
                self.cursor.append(nodo)
                if Q > 0:
                    self.cursor[Q].proximo = Q+1 #encadenamiento de libres

            self.cursor[alSize].proximo  = NULO #el proximo del ultimo es nulo(en este caso)    

            self.inicio = NULO
            self.final = NULO
            self.libre = MIN #el primer nodo libre

            super().__init__(TipoClave, alSize)
    

    def siguiente(self, P:PosicionLista) -> PosicionLista:
        '''Proximo de P o NULO'''
        if self.EsVacia() or P == NULO:
            Q = NULO
        else:
            Q = self.cursor[P].proximo
        return Q


    def Anterior(self, P:PosicionLista)-> PosicionLista:
        '''Anterior de P o NULO'''
        if self.EsVacia() or P == NULO:
            Q = NULO
        else:
            Q = self.cursor[P].anterior
        return Q


    def Agregar(self, x:TipoElemento) -> Resultado:
        '''Agrega un item al final de la lista'''
        Result = Resultado.CError
        if x.TipoDatoClave(x.clave) != self.TipoDeDato:
            Result = Resultado.ClaveIncompatible
        elif not self.EsLlena():
            Q = self.libre #al principio es 1
            self.libre = self.cursor[Q].proximo
            self.cursor[Q].dato = x
            self.cursor[Q].proximo = NULO
            self.cursor[Q].anterior = self.final #si tengo una lista de 2 y agrego1, el ANTERIOR FINAL es el ultimo.

            if self.EsVacia():
                self.inicio = Q
            else:
                self.cursor[self.final].proximo = Q
            self.final = Q
            self.q_items += 1
            Result = Resultado.OK
        else:
            Result = Resultado.Llena
        return Result

    def ValidarPosicion(self, P:PosicionLista) -> bool:
        Encontre = False
        if not self.EsVacia():
            Q = self.inicio
            while Q != NULO and not Encontre:
                if Q == P:
                    Encontre = True
                else:
                    Q = self.cursor[Q].proximo
        return Encontre
        

    def Insertar(self, x:TipoElemento, P:PosicionLista) -> Resultado:
        '''Inserta un elemento en cualquier lugar de la lista'''
        Result = Resultado.CError
        if x.TipoDatoClave(x.clave) != self.TipoDeDato:
            Result = Resultado.ClaveIncompatible
        elif self.EsLlena():
            Result = Resultado.Llena
        elif self.ValidarPosicion(P):
            Q = self.libre
            self.libre = self.cursor[Q].proximo
            self.cursor[Q].dato = x
            self.cursor[Q].proximo = P
            self.cursor[Q].anterior = self.cursor[P].anterior
            self.cursor[P].anterior = Q
            if P == self.inicio:
                self.inicio = Q
            else:
                self.cursor[self.cursor[Q].anterior].proximo = Q
            self.q_items += 1
            Result = Resultado.OK
        else:
            Result = Resultado.PosicionInvalida
        return Result

    def Eliminar(self, P:PosicionLista) ->Resultado:
        Result = Resultado.CError
        if self.EsVacia():
            Result = Resultado.Vacia
        elif self.ValidarPosicion(P):
            Q = P
            if P == self.inicio and P == self.final:
                self.__init__(self.TipoDeDato,self.Size)
            else:
                if P == self.inicio:
                    self.inicio = self.cursor[self.inicio].proximo
                    self.cursor[self.inicio].anterior = NULO
                elif P == self.final:
                    self.final = self.cursor[self.final].anterior
                    self.cursor[self.final].prox = self.cursor[P].proximo
                else:
                    self.cursor[self.cursor[P].anterior].proximo = self.cursor[P].proximo
                    self.cursor[self.cursor[P].proximo].anterior = self.cursor[P].anterior
                self.cursor[Q].proximo = self.libre
                self.libre = Q

            self.q_items -= 1
            Result = Resultado.OK
        else:
            Result = Resultado.PosicionInvalida
        return Result

    def Buscar(self, x:TipoElemento) -> PosicionLista:
        Result = NULO
        if x.TipoDatoClave(x.clave) == self.TipoDeDato:
            Q =self.inicio
            Encontre = False
            while Q != NULO and not Encontre:
                if self.cursor[Q].dato.clave != x.clave:
                    Q = self.cursor[Q].proximo
                else:
                    Encontre = True
            if Encontre:
                Result = Q
        return Result

    def Recuperar(self, P:PosicionLista) -> TipoElemento:
        if P != NULO and self.ValidarPosicion(P):
            x = self.cursor[P].dato
        else:
            x = TipoElemento()
            x.TipoElementoVacio
        return x
    
    def Actualizar(self, x:TipoElemento, P:PosicionLista) -> Resultado:
        Result = Resultado.CError
        if x.TipoDatoClave(x.clave) != self.TipoDeDato:
            Result = Resultado.ClaveIncompatible
        elif self.EsVacia():
            Result = Resultado.Vacia
        elif P != NULO and self.ValidarPosicion(P):
            self.cursor[P].dato = x
            Result = Resultado.OK
        else:
            Result = Resultado.PosicionInvalida
        return Result

    def Ordinal(self, PLogica:int) -> PosicionLista:
        Result = NULO
        if not self.EsVacia():
            I = 1
            Q = self.inicio
            while I < PLogica and Q != NULO:
                I += 1
                Q = self.cursor[Q].proximo
            if Q != NULO:
                Result = Q
        return Result

    def Intercambio(self, P:PosicionLista, Q:PosicionLista):
        X1 = self.cursor[P].datos
        X2 = self.cursor[Q].datos
        self.cursor[P].dato = X2
        self.cursor[Q].dato = X1

    def Sort(self,Ascendente:bool):
        P = self.inicio
        while P != NULO:
            Q = self.inicio
            while Q != NULO:
                X1 = self.cursor[Q].dato
                if self.siguiente(Q) != NULO:
                    X2 = self.cursor[self.cursor[Q].proximo].dato
                    if Ascendente:
                        if X1.clave > X2.clave:
                            self.Intercambio(Q, self.cursor[Q].proximo)
                    else:
                        if X1.clave < X2.clave:
                            self.Intercambio(Q, self.cursor[Q].proximo)
                Q = self.cursor[Q].proximo
            P = self.cursor[P].proximo

    def Comienzo(self) -> PosicionLista:
        return self.inicio

    def Fin(self) -> PosicionLista:
        return self.final