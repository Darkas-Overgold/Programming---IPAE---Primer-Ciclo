##Se ingresan notas, desarrolle un algoritmo que permita mostrar cuantos
##aprobaron el curso, considerar que el programa se termina automáticamente si
##se ingresa una nota errada.
na=0
nd=0
print('===============================')
while(True):
  nota=float(input('Ingrese nota : '))
  if(nota<0 or nota>20):
    ##nota invalida!!!
    print('Ingresaste una nota invalida 😢')
    break
  if(nota>=10.5):
    na=na+1
  else:
    nd=nd+1
print('===============================')
print('Resultados')
print('Numero aprobados :', na)
print('Numero desaprobados :', nd)