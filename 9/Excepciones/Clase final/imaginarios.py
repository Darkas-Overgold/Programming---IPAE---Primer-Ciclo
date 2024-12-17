#raiz cuadrada de numeros negativos

try:
  n=-9
  r=n**(1/2)
  print(r)
except Exception as error:
  print(error)
  print('error')

#ganancias del dia

v=int(input('ingrese ventas de hoy :' ))

try:
  if(v<0):
    raise Exception('El monto no puede negativo')
except:
  print('Ha surgido un error 😢')