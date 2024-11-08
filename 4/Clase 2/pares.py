#Crear un programa que solicite al usuario dos números enteros y muestre todos los números pares en el intervalo [a, b]
# Solicitar el primer número y validar con isdigit()
while True:
    a = input("Ingrese un número: ")
    if a.isdigit():
        a = int(a)
        break
    else:
        print("Entrada no válida. Por favor, ingrese un número.")
# Solicitar el segundo número y validar con isdigit()
while True:
    b = input("Ingrese otro número: ")
    if b.isdigit():
        b = int(b)
        break
    else:
        print("Entrada no válida. Por favor, ingrese un número.")
# Mostrar números pares en el intervalo [a, b]
i = a
while i <= b:
    if i % 2 == 0:
        print("Número par:", i)
    i += 1