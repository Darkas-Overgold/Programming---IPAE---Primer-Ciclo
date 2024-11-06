#solicitar 5 edades por teclado
#¿Cuántos son mayor de edad?
#¿Cuántos son menor de edad?
mayor = 0
menor = 0
for x in range(1, 6):
    while True:
        try:
            n = int(input(f'Ingrese edad {x}: '))
            if n >= 0:  # Verifica que la edad sea un número positivo
                break
            else:
                print("Por favor, ingrese una edad válida (número positivo).")
        except ValueError:
            print("Por favor, ingrese solo números.")
    if n < 18:
        menor += 1
    else:
        mayor += 1
print('=' * 30)
print('Cantidad de mayores de edad:', mayor)
print('Cantidad de menores de edad:', menor)