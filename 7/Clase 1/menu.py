#Implementar un menú
def triangulo(b,h):
  s=b*h/2
  return s
def cuadrado(a):
  s=a*a
  return s
def circulo(r):
  s=3.141592*r*r
  return s
print('='*20)
print('menu'.center(20))
print('='*20)
print(' 1 : Triangulo')
print(' 2 : Cuadrado')
print(' 3 : Círculo')
print(' 0 : Salir')
print('='*20)
opcion=input('opcion : ')
if(opcion=='0'):
  print('Fin del programa')
if(opcion=='1'):
  #triangulo
  b=int(input('Ingrese la base : '))
  h=int(input('Ingrese la altura : '))
  s=triangulo(b,h)
  print('el area es :', s)
if(opcion=='2'):
  #triangulo
  a=int(input('Ingrese el lado : '))
  s=cuadrado(a)
  print('el area es :', s)
if(opcion=='3'):
  #triangulo
  a=int(input('Ingrese el radio : '))
  s=circulo(a)
  print('el area es :', s)