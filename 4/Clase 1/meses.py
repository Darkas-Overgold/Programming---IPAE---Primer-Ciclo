#solicitar al usuario
#ingresar 6 números
#indicar si el número ingresado representa un número de mes
for x in range(1, 7):
    while True:
        try:
            n = int(input(f'Ingrese número {x}: '))
            break  # Si es un número válido, sale del bucle
        except ValueError:
            print("Por favor, ingrese solo números.")
    if 1 <= n <= 12:
        print(n, 'sí es un número de mes.')
    else:
        print(n, 'no es un número de mes.')