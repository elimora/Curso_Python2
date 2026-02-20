print("--- Clasificación de Categoría de Boxeo ---\n")

# Pedir el peso al usuario
peso = float(input("Ingresa el peso del boxeador en kg: "))

# 1. Validación de rango
if peso < 40 or peso > 150:
    print("Peso fuera de rango competitivo")

# 2. Categorización usando elif
elif peso >= 91:
    print("Categoría: Peso Pesado")

elif peso >= 75:
    print("Categoría: Peso Medio")

elif peso >= 60:
    print("Categoría: Peso Ligero")

elif peso >= 48:
    print("Categoría: Peso Mosca")

# 3. Caso por defecto
else:
    print("Categoría: Infantil o Amateur")
