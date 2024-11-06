#Dado un numero de dos digitos, hallar la suma de los digitos 😀
import sys
sys.stdout.reconfigure(encoding='utf-8')
numero = int(input("Ingrese un número de dos dígitos: "))
decenas = numero // 10
unidades = numero % 10
suma_digitos = decenas + unidades
invertido = unidades * 10 + decenas
print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
print(f"El número invertido de {numero} es: {invertido}")