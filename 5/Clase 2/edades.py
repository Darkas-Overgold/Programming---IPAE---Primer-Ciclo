# h) Se ingresa la edad de 100 personas (mínimo 0 años, máximo 150 años),
# indicar que cantidad de edades ingresadas pertenecen a cada etapa del
# desarrollo humano, queda a criterio el colocar si toma o no el extremo
# (NO considerar la etapa Prenatal).
import random as rnd
ni = 0
na = 0
nj = 0
nz = 0
nv = 0
print("=" * 20)
for x in range(100):
    edad = rnd.randint(0, 150)
    print(x, edad, sep="\t")
    if 0 <= edad < 12:
        ##infancia
        ni = ni + 1
    if 12 <= edad < 18:
        ##adolecencia
        na = na + 1
    if 18 <= edad < 25:
        ##juventud
        nj = nj + 1
    if 25 <= edad < 65:
        ##adultez
        nz = nz + 1
    if 65 <= edad:
        ##vegez
        nv = nv + 1
print("=" * 20)
print("resultados :")
print("=" * 20)
print("infancia", ni, sep="\t")
print("adolecencia", na, sep="\t")
print("juventud", nj, sep="\t")
print("adultez", nz, sep="\t")
print("vejez", nv, sep="\t")
print("=" * 20)