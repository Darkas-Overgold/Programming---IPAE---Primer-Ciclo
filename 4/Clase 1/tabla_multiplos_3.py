#Hallar la tabla multiplicar de un numero ingresado por teclado de los numeros multiplos de 3
while True:
    try:
        n = int(input('Ingrese un número: '))
        break  # Si es un número válido, sale del bucle
    except ValueError:
        print("Por favor, ingrese solo números.")
for x in range(3, 10, 3):
    print(f'{n} * {x} = {n * x}')