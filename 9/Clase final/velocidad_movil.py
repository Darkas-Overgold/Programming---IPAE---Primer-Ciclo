#ejercicio 3
#elaborar un algoritmo para el calculo
# de la velocidad de un movil
# Función para calcular la velocidad
def calcular_velocidad(distancia, tiempo):
    return distancia / tiempo

# Bucle para obtener entrada de datos y calcular la velocidad
while True:
    try:
        # Solicitar al usuario la distancia
        distancia = float(input("Introduce la distancia recorrida en metros (o 'salir' para terminar): "))

        # Solicitar al usuario el tiempo
        tiempo = float(input("Introduce el tiempo empleado en segundos: "))

        # Validar si el tiempo es cero
        if tiempo == 0:
            print("El tiempo no puede ser cero. Por favor, ingresa un valor mayor que cero.")
            continue

        if tiempo <= 0:
            print("El tiempo no puede ser negativo. Por favor, ingresa un valor positivo.")
            continue

        # Calcular la velocidad
        velocidad = calcular_velocidad(distancia, tiempo)

        # Mostrar el resultado
        print(f"La velocidad del móvil es: {velocidad:.2f} metros por segundo.")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa números válidos.")

    # Preguntar al usuario si desea continuar o salir
    continuar = input("¿Quieres calcular otra velocidad? (sí/no): ").lower()
    if continuar != 'sí':
        print("Gracias por usar el programa.")
        break