# Ejercicio G - propuesto: Hallar el cuadrante de una coordenada
def es_numero_valido(entrada):
    # Verifica si la entrada es un número float o negativo
    try:
        float(entrada)
        return True
    except ValueError:
        return False
# Solicitar y validar la coordenada x
while True:
    x_input = input('Ingrese coordenada x: ')
    if es_numero_valido(x_input):
        x = float(x_input)
        break
    else:
        print("Entrada no válida. Por favor, ingrese un número (puede ser float o negativo).")
# Solicitar y validar la coordenada y
while True:
    y_input = input('Ingrese coordenada y: ')
    if es_numero_valido(y_input):
        y = float(y_input)
        break
    else:
        print("Entrada no válida. Por favor, ingrese un número (puede ser float o negativo).")
cuadrante = ''
# Determinar el cuadrante
if x == 0 and y == 0:
    cuadrante = 'Orígen'
elif x > 0:
    if y > 0:
        cuadrante = 'Primer'
    else:
        cuadrante = 'Cuarto'
else:  # x < 0
    if y > 0:
        cuadrante = 'Segundo'
    else:
        cuadrante = 'Tercer'
print(cuadrante, 'cuadrante')