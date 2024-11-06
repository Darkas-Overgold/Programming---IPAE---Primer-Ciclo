x=int(input("Ingrese su edad: "))
if((25<=x)and(x<=60)):
    print("Usted es adulto")
else:
    if((0<=x)and(x<25)):
        print("Usted es menor de edad")
    else:
        print("Usted es mayor de edad")