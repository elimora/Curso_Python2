# * LISTAS: (Arrys, Vectores, Arreglo)

# * Creacion de las Listas
lista_numros = [1, 2, 3, 4, '5', False]
print(lista_numros)

# * Uso de las listas
# * Identificar posición
print(lista_numros[5])
print(lista_numros[-2])

# * Modificacion de un elemento
lista_numros[-2] = 5
print(lista_numros[-2])

# * Tipo de Dato de una lista
print("TDD de la lista ", type(lista_numros))

# * Longitud
print(len(lista_numros))

# * Agregar elementos a una lista (append) agrega el elemento al final
lista_vacia = []  # ! lista_vacia [0] = "Hola" error
lista_vacia.append("Hola")
print(lista_vacia)

lista = [3, 1, 4]
lista.append(2)
print(lista)

# pop (borrar)
print(lista.pop())
print(lista)

# sort (ordenar)
lista.sort(reverse=False)
print(lista)

# *Index
print(lista.index(4))


print("Desde aca TUPLAS")
# ? **************Tuplas****************
tupla_numeros = (1, 2, 3, 4, '5', False)
print(tupla_numeros)
tupla = 1, 2, True

# * Utilidad de la Tutlas

# *Acceso a la s Tuplas, mediante sus indices
print(tupla_numeros[5])
print(tupla_numeros[-2])
#! No PODEMOS MODIFICAR LA TUPLAS
#!tupla_numeros[-2] = 5

# * Tipo de Datos (type)
print("Tipo de datos de una tupla:", type(tupla_numeros))

# * Lomgitud
print(len(tupla_numeros))

# * Metodos CONSTRUCTORES: list(elemento_iterable), tuple(elemento_iterabe)

print("-----METODOS CONSTRUCTORES-----")
print("Tupla", tupla_numeros)
lista_desde_tupla = list(tupla_numeros)
print("Lista desde una Tupla", lista_desde_tupla)

print("Lista", lista_numros)
tupla_desde_lista = tuple(lista_numros)
print("Tupla desde una lista", tupla_desde_lista)
