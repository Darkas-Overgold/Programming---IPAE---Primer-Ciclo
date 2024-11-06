#Calcular densidad
x=float(input('Ingrese la coordenada x: '))
y=float(input('Ingrese la coordenada y: '))
z=float(input('Ingrese la coordenada z: '))
densidad=((1)/(x*y+x*z+y*z))**3 + ((x+y+z)/((1/x)+(1/y)+(1/z)))**4
print('La densidad es :', densidad)