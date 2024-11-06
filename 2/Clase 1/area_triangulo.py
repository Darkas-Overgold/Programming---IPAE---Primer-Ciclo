import sys
sys.stdout.reconfigure(encoding='utf-8')
# Calcular el área de un triángulo
b = float(input('Ingrese la base del triángulo: '))
h = float(input('Ingrese la altura del triángulo: '))
s = b * h / 2
print('El área del triángulo es:', s)