##agregar validacion de mayoria de edad!
alumnos=['Maria','Jose','Pedro','Victor','Fio']
indices=[0,1,2,3,4]
edades=[]
for x in alumnos:
  edad=int(input(f'Ingrese edad de {x} : '))
  while(edad<0 or edad>100):
    print('Edad incorrecta 😢')
    edad=int(input(f'Re-ingrese edad de {x} : '))
  edades.append(edad)
##mostrar reporte!!!
print('o'*40)
for x in indices:
  mensaje='Mayor de Edad'
  if(edades[x]<18):
    mensaje='Menor de edad'
  print(alumnos[x] , edades[x], mensaje, sep='\t')
print('o'*40)