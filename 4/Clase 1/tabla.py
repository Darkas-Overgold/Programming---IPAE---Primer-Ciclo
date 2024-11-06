#Calcular la tabla de multiplicación de un número ingresado por teclado
while True:
    try:
        n = int(input('Ingrese un número: '))
        break  # Si la conversión es exitosa, salimos del bucle
    except ValueError:
        print("Por favor, ingrese solo números.")  # Mensaje de error si la entrada no es un número
for x in range(1, 11):
    print(f'{n} * {x} = {n * x}')