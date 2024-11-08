#Validar que tres números ingresados den como suma 10
while True:
    numeros = []  # Lista para almacenar los tres números
    # Usar un bucle for para pedir tres números
    for i in range(1, 4):
        while True:
            numero = input(f"Ingrese el número {i}: ")
            if numero.isdigit():
                numeros.append(int(numero))  # Convertir a entero y agregar a la lista
                break  # Salir del bucle while si la entrada es válida
            else:
                print("Entrada no válida. Por favor, ingresa solo números.")
    # Calcular la suma de los tres números
    suma = sum(numeros)
    # Verificar si la suma es 10
    if suma == 10:
        print("¡La suma de los tres números es 10!")
        break  # Salir del bucle principal si la suma es 10
    else:
        print("La suma de los tres números no es 10. Inténtalo de nuevo.")