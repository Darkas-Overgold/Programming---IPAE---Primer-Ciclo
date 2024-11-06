#Dada una temperatruta expresada en grados celcius, hallar su equivalente en grados Fahrenheit
import sys
sys.stdout.reconfigure(encoding='utf-8')
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
# Fórmula de conversión a Fahrenheit
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")