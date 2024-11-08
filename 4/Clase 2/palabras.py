#Validar si una palabra tiene 2 vocales
while True:
    # Pedir al usuario que ingrese una palabra
    palabra = input("Ingresa una palabra: ")
    # Validar que la palabra contenga solo letras
    if palabra.isalpha():
        # Convertir la palabra a minúsculas para simplificar la verificación de vocales
        palabra = palabra.lower()
        # Contar las vocales en la palabra
        contador_vocales = sum(1 for letra in palabra if letra in "aeiou")
        # Verificar si hay exactamente dos vocales
        if contador_vocales == 2:
            print("La palabra contiene exactamente dos vocales.")
        else:
            print("La palabra no contiene exactamente dos vocales.")
            palabra = input("Reingresa una palabra: ")
        break  # Salir del bucle si la palabra es válida
    else:
        print("Entrada no válida. Por favor, ingresa solo letras.")