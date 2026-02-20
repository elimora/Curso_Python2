# *For

lista = [1, 2, 3, 4, 5]

# ? recorrer los elemento
for elemento in lista:
    print("Elemento - ", elemento)

print("-----Cuadrados-----")
# ?Hacer calculos en cada vuelta
for ele in lista:
    print("Elevado", ele**2)

# *Poblar un iterable
lista = [1, 2, 3, 4, 5]
lista_nueva = []

for ele in lista:
    lista_nueva.append(ele**2)

print(lista_nueva)

# * Puedes colocar condicionales
for ele in lista:
    if ele % 2 == 0:
        print(F"Los pares dentro de las lista son {ele}")

# * Sentencias de Control dentro de un BUCLE
# ? Break
lista = [1, 2, 3, 4, 5]
for i in lista:
    if i == 3:
        break
    print(f'imprimiendo hasta el 2, elemento = {i}')

# ? continue  "Salta un elemento que encuentre"
for i in lista:
    if i == 3:
        continue
    print(f'Imprimimos el elemento, ele = {i}')
print("✋Hemos salidos del bucle for con el continue")
