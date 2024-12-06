#ejercicio 4
#calcular el interés compuesto de un monto
def interes(monto):
  for x in range(12):
    monto=monto+monto*0.037
  return monto
capital=float(input('Ingrese su capital : '))
print('el monto es : ', interes(capital))