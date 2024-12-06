#implementar un sistema de notas
#nombre, nota
#ingresar nota, listar notas
#mostrar estadisticas

from IPython.display import clear_output
import math
import matplotlib.pyplot as plt

nombres=[]
notas=[]

while (True):
  #menu:
  print("="*25)
  print('menu'.center(25))
  print("="*25)
  print(' 1 : agregar')
  print(' 2 : listar')
  print(' 3 : estadisticas')
  print(' 0 : salir')
  print("="*25)
  opcion=input('opcion : ')
  # clear_output()

  if(opcion=='0'):
    print('fin del programa 😢')
    break

  if(opcion=='1'):
    #ingresar nombre, nota
    nombre=input('Ingrese nombre : ')
    nota=int(input('Ingrese nota : '))

    nombres.append(nombre)
    notas.append(nota)

  if(opcion=='2'):
    #listar
    print('nombre', 'nota' , sep='\t')
    print('-'*20)
    for nombre, nota in zip(nombres, notas):
      print(nombre, nota , sep='\t')

  if(opcion=='3'):
    #estadisticas
    minima=min(notas)
    maximo=max(notas)
    promedio= sum(notas)/len(notas)
    print('resultados'.center(20))
    print('minima : ', minima)
    print('maximo : ', maximo)
    print('promedio : ', promedio)