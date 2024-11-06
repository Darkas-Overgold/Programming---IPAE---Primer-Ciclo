import sys
import math
sys.stdout.reconfigure(encoding='utf-8')
# Calcular el volumen de un cilindro
radio = float(input('Ingrese el radio de la base del cilindro: '))
altura = float(input('Ingrese la altura del cilindro: '))
# Fórmula del volumen del cilindro: V = π * r^2 * h
volumen = math.pi * radio**2 * altura
print("El volumen del cilindro es:", volumen)