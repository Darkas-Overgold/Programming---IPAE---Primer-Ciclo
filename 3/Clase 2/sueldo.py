from re import sub
# Ejercicio 3: Solicitar categoría y número de hijos, con validaciones de entrada
print('====================')
print('Categorias: ')
print('====================')
print(' A :  1100')
print(' B :  2000')
print(' C :  3500')
print('====================')
# Solicitar y validar la categoría
while True:
    categoria = input('Seleccione (A, B, C): ').upper()
    if categoria.isalpha() and categoria in ['A', 'B', 'C']:
        break
    else:
        print("Entrada no válida. Por favor, ingrese una letra válida (A, B o C).")
print('')
sueldo = 0
if categoria == 'A':
    sueldo = 1100
elif categoria == 'B':
    sueldo = 2000
elif categoria == 'C':
    sueldo = 3500
# Solicitar y validar el número de hijos
print('====================')
print('Numero de hijos: ')
print('====================')
print(' 1         :  0%')
print(' 2,3,4     :  20%')
print(' mas de 4  :  22%')
print('====================')
while True:
    hijos_input = input('Numero de hijos: ')
    if hijos_input.isdigit():
        hijos = int(hijos_input)
        break
    else:
        print("Entrada no válida. Por favor, ingrese un número.")
print('')
bonificacion = 0
if hijos == 1:
    bonificacion = 0
elif hijos <= 4:
    bonificacion = 0.2
else:
    bonificacion = 0.22
subtotal = sueldo + sueldo * bonificacion
# Calculo de descuento en base a la AFP
print('====================')
print('AFP : ')
print('====================')
print(' 1 : PRIMA     12%')
print(' 2 : UNION     13%')
print(' 3 : HORIZONTE 12.7%')
print(' 4 : INTEGRA   13.9%')
print('====================')
afp = input('Seleccione: ')
print('')
descuento = 0
if afp == '1':
    descuento = 0.12
elif afp == '2':
    descuento = 0.13
elif afp == '3':
    descuento = 0.127
elif afp == '4':
    descuento = 0.139
# Calcular monto total a pagar
total = subtotal - subtotal * descuento
print('El neto a pagar es:', total)