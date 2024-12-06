#implementar las 4 operaciones básicas con funciones
#considerar dos números como entradas
def suma(a,b):
  return a+b
def resta(a,b):
  return a-b
def multiplicacion(a,b):
  return a*b
def division(a,b):
  return a/b
print('============================')
a=int(input('ingrese numero a : '))
b=int(input('ingrese numero b : '))
print('============================')
print('suma : ', suma(a,b))
print('resta : ', resta(a,b))
print('multiplicacion : ', multiplicacion(a,b))
print('division : ', division(a,b))
print('============================')