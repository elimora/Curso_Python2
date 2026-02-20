# ****Ejemplo de Menu de Opciones
VERDE = "\033[32m"
AZUL = "\033[34m"
CYAN = "\033[36m"
ROJO = "\033[31m"
AMARILLO = "\033[33m"
RESET = "\033[0m"

while True:
    print(f'{AZUL}  -------Menú de Opciones--------{RESET}')
    print('1. Ver perfil')
    print('2. Cargar datos')
    print('3. Visualización')
    print('4. Salir')

    opcion = input(f'\n{CYAN} Por favor, digite una opcion {{1-4}}: {RESET}')
    match  opcion:
        case 'a' | 'b' | 'c':
            print(f'{ROJO} NADA DE LETRAS 😡 .....{RESET}')
        case '1':
            print(f'{VERDE} Viendo el Perfil  .....{RESET}')
        case '2':
            print(f'{VERDE} Cargar Datos  .....{RESET}')
        case '3':
            print(f'{VERDE} Visualización preparada  .....{RESET}')
        case '4':
            print(f'{ROJO} Saliendo del Programa  .....{RESET}')
            break
        case _:
            print(
                f'{AMARILLO} 🚩 Error: Opcion no valida. Intenete de Nuevo  .....{RESET}')
