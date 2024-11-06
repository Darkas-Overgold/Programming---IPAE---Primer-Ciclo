#Calcular velocidad
a=float(input('Ingrese la coordenada a: '))
b=float(input('Ingrese la coordenada b: '))
velocidad=((a+b)/(a-b))**2 + ((a+a*b)/(a-1/b)) + ((1)/(a+b))
print('La velocidad es: ', velocidad)