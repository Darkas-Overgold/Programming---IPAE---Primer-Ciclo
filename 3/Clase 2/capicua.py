# EJERCICIO 4: Determinar si un número de 4 dígitos es capicúa
# Solicitar y validar la entrada para que sea un número de 4 dígitos
while True:
    abcd = input('Ingrese un número de 4 dígitos: ')
    if abcd.isdigit() and len(abcd) == 4:
        abcd = int(abcd)
        break
    else:
        print('Entrada no válida. Por favor, ingrese un número de 4 dígitos.')
# Verificar si el número es capicúa
d = abcd % 10
abc = abcd // 10
c = abc % 10
ab = abc // 10
b = ab % 10
a = ab // 10
if a == d and b == c:
    print('Es un número capicúa 😀')
else:
    print('No es un número capicúa 😢')