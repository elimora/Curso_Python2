# 1.- Listas Arrys, vectores, arreglos, matrices (mutables)
# 2.- Tuplas (tuple)
# 3.- Metodos CONSTRUTORES: list(mi_iterable) , tuple(mi_iterable)

# ? Metodos vistos en las listas
# append(ele)
# pop([indx]) eliminar
# remove(ele) elimina la primera ocurrencia
# index(ele, [start, end])

#!Metodos Nuevos
# ? Metodo insert(indice, elementos)
lista = [1, 3, 4, 5]
lista.insert(1, 2)
print(lista)

# ? Metodo extend(['elemento1', 'elemento2'...])
lista2 = [6, 7, 8]
lista.extend(lista2)
print(lista)

# ? Metodo sorted(lista) y su diferencia con el metodo sort()
# *.sort(): Modifica el iterable original, Ordenar en el sitio
# * sorted(): crea una copia y la retorna. Notoca a la lista orignal
# podria asignar lo que entraga a una variable
print(sorted(lista,  reverse=True))
print(lista.sort(reverse=True))  # None
print(lista)

# ? Metoso map(funcion, iterable)


def calcular_cubo(numero):
    return numero**3


lista_cubos = list(map(calcular_cubo, lista))
print(lista_cubos)

#! *****************TDD (tipos de datos) ESTRUCTURALES: STR CADENA DE TEXTO
nombre = 'Rodolfo'
print(len(nombre))
print(nombre[0])
nombre[1] = 'a'
