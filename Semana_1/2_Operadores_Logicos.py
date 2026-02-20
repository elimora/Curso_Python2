# * *****Operadores de Comparacion en Py(==, !=, <,>, <=, >=) bool

# * Comparacion Tipo de Datos Numericos:
# print(4 == 4)
# print(4 >= 4.0)
# print(5 > 3)
# print(5 > 5.0)
# print(5 != 5.0)

# * Comparacion Tipo de Datos boll:
# Se tratan como 1 (True) y 0 (False)
# print(True > False)

# * Comparacion Tipo de Datos str:
# print("hola" == "hola")
# print("hola" == "Hola")

# * Comparacion Tipo de Datos Caracter a Caracter:
# print(ord("A"))
# print(ord("a"))

# print("A" < "a")

# * La comparacion se realiza en orden:
# print(ord("a"), ord("b"), ord("c"), ord("d"))
# print("abc" < "abd")
# print(ord("M"))
# print(ord("M") == 78)

# * Comparacion entra cadenas:
# print("M" < 77)

# Los operadores de comparación devuelven true o falso.
# Debes comparar preferentemente valores del mismo tipo para evitar errores.
# Para cadenas, la comparación es lexicográfica, sensible a mayúsculas y minúsculas.
# De tipos numéricos, se comportan naturalmente según el valor.
# == y ¡= pueden comparar distintos tipos pero otros operadores no pueden hacerlo.

# * Operadores de Comparacion e Igualdad(adelanto de Condicionales, strip(), lower())
# Comparador de palabras que pida dos palabras y verique si son identicas

print("🔎 COMPARADOR DE PALABRAS IGNORANDO CAPITALIZACION")
print("="*47)

# * Input 1
palabra1 = input("Ingrese la primera palabra: ").strip().lower()

# * Input 2
palabra2 = input("Ingrese la segunda palabra: ").strip().lower()

# * Comparacion

if palabra1 == palabra2:
    print("Las palabras son Identicas 👋")
else:
    print("Las palabras son diferentes ❌")
    print(f"Palabra 1 {palabra1}")
    print(f"Palabra 2 {palabra2}")
