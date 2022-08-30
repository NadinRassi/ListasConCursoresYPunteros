from tipos import *
from listacursor import *

lista1 = Lista(TipoDatosClave.NUMERO, 3)#que tipo de datos guardo y la cantidad de nodos

x= TipoElemento()
x.clave = 5

while not lista1.EsLlena():
    lista1.Agregar(x)

print(lista1.ValidarPosicion(7)) #le estoy diciendo que me valide si hay una posicion 7
# En lista1 le dije que el tipo sera numero, pero con 3 lugares

print(lista1.CantidadElementos())
