#Hallar la suma de un intervalo de números ingresados por teclado
while True:
    try:
        a = int(input('Ingrese valor inicial: '))
        break
    except ValueError:
        print("Por favor, ingrese solo números.")
while True:
    try:
        b = int(input('Ingrese valor final: '))
        if b >= a:
            break
        else:
            print("El valor final debe ser mayor o igual que el valor inicial.")
    except ValueError:
        print("Por favor, ingrese solo números.")
s = 0
for x in range(a, b + 1):
    s += x
print('La suma es de:', s)
print('=' * 30)