#Validar si una palabra tiene vocales
while True:
    letra = input("Ingresa una vocal: ").lower()  # Convertir a minúscula
    # Verificar si la entrada es una vocal
    if letra in ['a', 'e', 'i', 'o', 'u']:
        print(f"'{letra}' es una vocal válida.")
        break
    else:
        print("Entrada no válida. Por favor, ingresa una vocal.")