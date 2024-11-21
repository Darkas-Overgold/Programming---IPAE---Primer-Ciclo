#ejercicio 4
#agregar 5 numeros a una lista
#indicar maximo y minimo

numeros=[]

for x in range(5):
  numero=int(input('Ingresar numero : '))
  numeros.append(numero)

maximo=0
minimo=numeros[0]
for numero in numeros:
  if(maximo<numero):
    maximo=numero
  if(minimo>numero):
    minimo=numero

print('===================')
print('maximo :', maximo)
print('maximo :', max(numeros))
print('===================')
print('minimo :', minimo)
print('minimo :', min(numeros))