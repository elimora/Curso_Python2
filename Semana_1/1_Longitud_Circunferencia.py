# ----Ejercicio Variables, CONSTANTES, Operaciones Matematicas (input(), formart y Modulos)
# Calculo de la Longitud de una Circunferencia

import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# ---Datos----
radio = float(input("Ingresa el radio de la Circunferencia: "))
PI = math.pi  # CONSTANTE
longitud = 2*PI*radio
color_cir = input("Ingrese el color de la circunferencia en ingles: ")
fill_cir = bool(int(input("Rellenamos el Circulo? (1/0): ")))

# ---Crear la figura: Lienzo o Canvas
# Destructuring
# fig = Objeto Figura (Ventana Completa)
# ax = El eje de referencia
fig, ax = plt.subplots()

# ---Crear el Circulo----
circulo = Circle((0, 0), radio, fill=fill_cir, color=color_cir, linewidth=2)

# ----Agregar el Circulo al Area de Dibujo, Aun con esto no vemos nada.
ax.add_patch(circulo)
fig.suptitle("Grafica de una Circunferencia", fontsize=12)

# ---Etiquetas
# --Usar formato de cifras {num:.2f}
ax.text(0, radio + 0.5, f'Longitud : {longitud:.2f}', ha='center', fontsize=12)

ax.set_aspect('equal')  # circunferencia perfecta sino me pone una elipse
ax.set_xlim(-1.5*radio, 1.5*radio)
ax.set_ylim(-1.5*radio, 1.5*radio)
ax.set_title(f'Circunferencia (r = {radio})')
plt.grid(True)
plt.show()
