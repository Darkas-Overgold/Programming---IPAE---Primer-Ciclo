sueldo = float(input("Ingrese monto del sueldo"))
tiempo = float(input("Ingrese su tiempo en la empresa"))
if(tiempo<1):
    bono = 0
if(1<= tiempo and tiempo <2):
    bono = 0.10
if(2<= tiempo and tiempo <3):
    bono = 0.15
if(3<= tiempo and tiempo <4):
    bono = 0.20
if(tiempo >= 5):
    bono = 0.35
monto = sueldo + sueldo*bono
print("El monto final es: ", monto)
