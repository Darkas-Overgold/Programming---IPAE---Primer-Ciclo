# c) Realizar un algoritmo que permita el ingreso 200 números de tres cifras cada uno, descomponerlos y determinar cuántos de los dígitos que componen cada número fueron pares y cuántos impares.
import random as rnd
print("Numero", "pares", "impares", sep="\t")
print("=" * 30)
for x in range(100):
    abc = rnd.randint(100, 999)
    c = abc % 10
    ab = abc // 10
    b = ab % 10
    a = ab // 10
    np = 0
    ni = 0
    if a % 2 == 0:
        np = np + 1
    else:
        ni = ni + 1
    if b % 2 == 0:
        np = np + 1
    else:
        ni = ni + 1
    if c % 2 == 0:
        np = np + 1
    else:
        ni = ni + 1
    print(abc, np, ni, sep="\t")