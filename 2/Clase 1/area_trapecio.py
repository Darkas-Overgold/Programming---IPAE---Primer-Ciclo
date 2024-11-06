import sys
sys.stdout.reconfigure(encoding='utf-8')
# Calcular el área de un trapecio
b_menor = float(input('Ingrese la base menor del trapecio: '))
b_mayor = float(input('Ingrese la base mayor del trapecio: '))
h = float(input('Ingrese la altura del trapecio: '))
# Fórmula del área del trapecio: A = ((B + b) * h) / 2
area = ((b_mayor + b_menor) * h) / 2
print("El área del trapecio es:", area)