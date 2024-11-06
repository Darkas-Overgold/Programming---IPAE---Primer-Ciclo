numero = input("Ingrese un número de 3 cifras: ")
if numero.isdigit() and len(numero) == 3:
    # Convertir el número a entero
    numero = int(numero)
    d1 = numero // 100
    d2 = (numero // 10) % 10
    d3 = numero % 10
    mayor = d1
    if d2 > mayor:
        mayor = d2
    if d3 > mayor:
        mayor = d3
    segundo_mayor = d1
    if (d2 > segundo_mayor and d2 < mayor) or (d2 < mayor and d1 == mayor):
        segundo_mayor = d2
    if (d3 > segundo_mayor and d3 < mayor) or (d3 < mayor and d1 == mayor):
        segundo_mayor = d3
    print("Número mayor:", mayor)
    print("Segundo dígito mayor:", segundo_mayor)
else:
    print("Error: Debe ingresar un número de exactamente 3 cifras.")