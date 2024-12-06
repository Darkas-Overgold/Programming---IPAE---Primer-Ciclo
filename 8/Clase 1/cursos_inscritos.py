#ejercicio 1
#definir diccionario de los cursos inscritos
cursos={}
cursos['Python']='Curso de Fundamentos de Programación empleando Python 3 con el profesor Irwin Iván Mendoza'
cursos['Lectura']='Curso de Lectura Comprensiva y Escritura con el profesor Percy Alberto Roa'
cursos['Desarrollo']='Curso de desarrollo personal con la profesora Elizabeth Vasquez Quiroga'
cursos['Web']='Curso de desarrollo web empleando html y css con el profesor Irwin Iván Mendoza'
cursos['Soporte']='Curso de implementacion de redes con packet tracer con el profesor Juan Alberto Pillaca'
cursos['Ofimatica']='Curso de herramientas de office con el profesor Juan William Ramos'
del cursos['Ofimatica']
#ejercicio 2
#mantenimiento de cursos
#diseñar un menu

cursos={}

while (True):
  print('='*20)
  print('cursos'.center(20))
  print('='*20)
  print(' 1 : Listar')
  print(' 2 : Agregar')
  print(' 3 : Modificar')
  print(' 4 : Eliminar')
  print(' 0 : Salir')
  print('='*20)
  opcion=input('Opción : ')

  if(opcion=='0'):
    print('Fin de programa xD')
    break

  if(opcion=='1'):
    #listar
    for x in cursos:
      print(x,'\t', cursos[x])

  if(opcion=='2'):
    #insertar
    codigo=input('Ingrese codigo del curso : ')
    nombre=input('Ingrese nombre del curso : ')
    cursos[codigo]=nombre

  if(opcion=='3'):
    #modificar

    codigo=input('Ingrese codigo del curso : ')
    nombre=input('Ingrese nuevo nombre del curso : ')
    if codigo in cursos.keys():
      cursos[codigo]=nombre
    else:
      print('Curso inexistente')

  if(opcion=='4'):
    #eliminar
    codigo=input('Ingrese codigo del curso : ')
    if codigo in cursos.keys():
      del cursos[codigo]
      print('curso eliminado con exito')
    else:
      print('Curso no existe')