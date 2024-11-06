#Mostrar los numeros pares e impares de un intervalo de numeros ingresados por teclado
while True:
    try:
        a = int(input('Ingrese valor inicial: '))
        break
    except ValueError:
        print("Por favor, ingrese solo números.")
while True:
    try:
        b = int(input('Ingrese valor final: '))
        if b > a:
            break
        else:
            print("El valor final debe ser mayor que el valor inicial.")
    except ValueError:
        print("Por favor, ingrese solo números.")
print("\nNúmeros pares en el intervalo:")
for x in range(a, b):
    if x % 2 == 0:
        print('Número par:', x)
print("\nNúmeros impares en el intervalo:")
for x in range(a, b):
    if x % 2 == 1:
        print('Número impar:', x)