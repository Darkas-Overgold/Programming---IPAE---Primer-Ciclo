#escribir un algoritmo
#para calcular la fuerza de un movil
m=float(input('Ingrese masa : '))
a=float(input('Ingrese asceleracion : '))
try:
  if(m==0):
    raise Exception()
  F=m*a
  print('fuerza : ', F)
except:
  print('La masa no puede ser cero 😢')