#Solicitar al usuario ingresar un texto
#Hallar la cantidad de vocales
#Hallar la cantidad de consonantes
consonante = 0
vocal = 0
while True:
    text = input('Ingrese el texto: ').lower()
    if text.isalpha():
        break  # Sale del bucle si el texto solo contiene letras
    else:
        print("Por favor, ingrese solo texto (sin números ni caracteres especiales).")
for letra in text:
    if letra in "aeiou":
        vocal += 1
    else:
        consonante += 1
print('Vocales:', vocal)
print('Consonantes:', consonante)