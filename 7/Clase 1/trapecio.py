#hallar el área de un trapecio con funciones
def trapecio(a,b,h):
  s=(a+b)*h/2
  return s
a=int(input('Ingrese base menor : '))
b=int(input('Ingrese base mayor : '))
h=int(input('Ingrese altura :'))
print('El área es : ', trapecio(a,b,h))