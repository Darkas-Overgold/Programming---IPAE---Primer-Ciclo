#Dado un numero de tres digitos, hallar la suma de digitos y el numero invertido
import sys
sys.stdout.reconfigure(encoding='utf-8')
numero = int(input("Ingrese un número de tres dígitos: "))
centenas = numero // 100
decenas = (numero // 10) % 10
unidades = numero % 10
suma_digitos = centenas + decenas + unidades
numero_invertido = unidades * 100 + decenas * 10 + centenas
print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
print(f"El número invertido de {numero} es: {numero_invertido}")