def tipo_triangulo(lado1, lado2, lado3):
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        if lado1 == lado2 == lado3:
            return "El triángulo es equilátero."
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "El triángulo es isósceles."
        else:
            return "El triángulo es escaleno."
    else:
        return "Los lados ingresados no forman un triángulo."
def obtener_lado(mensaje):
    while True:
        lado = input(mensaje)
        # Validación numérica
        if lado.replace('.', '', 1).isdigit() and lado.count('.') <= 1:
            return float(lado)
        else:
            print("Por favor, introduce un valor numérico válido.")
lado1 = obtener_lado("Introduce la longitud del primer lado: ")
lado2 = obtener_lado("Introduce la longitud del segundo lado: ")
lado3 = obtener_lado("Introduce la longitud del tercer lado: ")
# Tipo de triángulo
resultado = tipo_triangulo(lado1, lado2, lado3)
print(resultado)