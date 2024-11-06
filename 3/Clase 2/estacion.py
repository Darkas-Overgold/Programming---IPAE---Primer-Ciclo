# Ejercicio 2: Clasificación de las estaciones en base al número de mes.

print('=' * 20)
print('  1 : enero')
print('  2 : febrero')
print('  3 : marzo')
print('  4 : abril')
print('  5 : mayo')
print('  6 : junio')
print('  7 : julio')
print('  8 : agosto')
print('  9 : septiembre')
print(' 10 : octubre')
print(' 11 : noviembre')
print(' 12 : diciembre')
print('=' * 20)

# Solicitar entrada hasta que sea válida
while True:
    mes_input = input("Ingrese número de mes: ")
    
    # Verifica si la entrada es un número
    if mes_input.isdigit():
        mes = int(mes_input)
        if 1 <= mes <= 12:
            break  # Sale del bucle si la entrada es válida
        else:
            print("Número de mes incorrecto. Por favor, ingrese un número entre 1 y 12.")
    else:
        print("Entrada no válida. Por favor, ingrese un número.")

# Clasificación de la estación
if mes >= 1 and mes <= 3:
    estacion = 'verano'
elif mes >= 4 and mes <= 6:
    estacion = 'otoño'
elif mes >= 7 and mes <= 9:
    estacion = 'invierno'
elif mes >= 10 and mes <= 12:
    estacion = 'primavera'

print("La estación es:", estacion)
