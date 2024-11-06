# Ejercicio 5: Calcular el monto en base a la edad y tipo de sangre
# Solicitar y validar la edad
while True:
    edad_input = input('Ingrese su edad: ')
    if edad_input.isdigit() and int(edad_input) > 0:
        edad = int(edad_input)
        break
    else:
        print("Entrada no válida. Por favor, ingrese un número positivo para la edad.")
print('=================================')
# Solicitar y validar el grupo sanguíneo
while True:
    print('')
    print('GRUPO SANGUÍNEO')
    print('=================================')
    print('   A   :   Tipo A')
    print('   B   :   Tipo B')
    print('   AB  :   Tipo AB')
    print('=================================')
    tipo = input('Tipo: ').upper()  # Convertir la entrada a mayúsculas
    if tipo.isalpha() and tipo in ['A', 'B', 'AB']:
        break
    else:
        print("Entrada no válida. Por favor, ingrese un grupo sanguíneo válido (A, B, AB).")
# Calcular el monto en base a la edad y tipo de sangre
monto = 1800
if edad == 18 and tipo == 'A':
    monto = 3000
elif 19 <= edad <= 35 and tipo == 'A':
    monto = 1500
elif 19 <= edad <= 35 and tipo == 'B':
    monto = 2500
elif 36 <= edad <= 55 and (tipo == 'AB' or tipo == 'A'):
    monto = 4000
print('El monto final es:', monto)