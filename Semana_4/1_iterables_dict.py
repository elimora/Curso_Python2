# *****Tipo de Dato DICT (Diccionarios)
# ? key:value
# ? key son TDD Inmutables: str, int, bool, tuple
# ? Los datos se comparten en archivos de tipo json [{} {} {}]

personaje = {
    "nombre": "Mujer Maravilla",
    "edad": 28,
    'peso': 56.66,
    "altura": 1.8,
    "poderes": ['volar', 'super fuerza'],
    "mujer": False,
    "mujer": True,  # ?las key repetidas sobrescribe el valor
    2: 'Dos',
    False: 'falso',
    ('nota', 'materia'): ['20', 'programación'],  # ? tuplas como un key
    # * juego
    (0, 0): 'Inicio',
    (1, 5): 'Cofre de Oro',
    (10, 2): 'Enemigo final'
}

# ? Acceso a los valores mediante su claves o keys
print(personaje['nombre'])
print(personaje['edad'])
print(personaje[False])
print(personaje[2])
print(personaje[('nota', 'materia')])
print(personaje[('nota', 'materia')][1])

posicion = (1, 5)
print(f'En la posicion {posicion} hay : {personaje[posicion]}')

# ?TTD  type
print(type(personaje))
# *print(personaje)

print('************Recorriendo un Diccionario********')
for key in personaje:
    print(f'Clave: {key} - Valor: {personaje[key]}')


# ? 🎇Metodos Importantes para los Diccionarios
print('🎇Metodos Importantes para los Diccionarios')

# ? Metodo keys
print('Keys', personaje.keys())

print('*********Keys()**********\n')
for k in personaje.keys():
    print(k)

# ? Metodo Values
print('*********Values()**********\n')
for v in personaje.values():
    print(v)

# ? Metodos items()
print('*********Items entero**********\n')
for k, v in personaje.items():
    print(f'{k} -- {v}')

# ! Lista de  compresion   (MUY INPORTANTE ESTE FUNCION)

print('********Lista de Compresión**********')
mi_lista = list((k, v) for k, v in personaje.items())
print(mi_lista)

mi_lista_values = list(v for v in personaje.values())
mi_lista_keys = list(k for k in personaje.keys())

print('\n******** Values y keys mediante  Compresión**********')

print('\n Lista de valores del diccionario')
print(mi_lista_values)
print('\n Lista de keys del diccionario')
print(mi_lista_keys)

# ?Slice Sintaxis [inicio: fin: paso]
print('\n****** SLIDE*********')
keys = mi_lista_keys[:4]
print(keys)

#! Zip Usada para emparejar y comprimir para construir un diccionario
values = ['Hombre Araña', 19, 70.70, ['Trepar', 'Tejer']]

mi_dic_hom_ara = {k: v for k, v in zip(keys, values)}

print('\n ZIP Hombre araña LARGO')
print(mi_dic_hom_ara)

#! Construcctor de Diccionrios (dict) mas rapida

mi_dic = dict(zip(keys, values))

print('\n****Zip mejorado, nediante Dict(Constructor de diccionarios)***')
print(mi_dic)

#! Crear un Personaje con DICT
personaje_2 = dict(nombre="Thor", edad=1500, mujer=False)
print(personaje_2)

#!Otra forma de Acceder a los elementos de un Diccionario key y get()
# print(personaje['hobbie'])
print(personaje.get('altura'))
print(personaje.get('hobbie', "No se encontro el valor indicado"))
