##ejercicio 2
##validar el ingreso de 5 vocales
##mostrar un resumen general
vocales=['a','e','i','o','u']
ingresados=[]
resumen=[0,0,0,0,0]
for x in range(1,6):
  vocal=input(f'{x} - Ingresa una vocal : ').lower()
  while(not vocal.isalpha()):
    print('letra ingresada no valida 😢')
    vocal=input(f'{x} - Re ingresa una vocal : ').lower()
  while(vocal not in vocales):
    print('letra ingresada no valida 😢')
    vocal=input(f'{x} - Re ingresa una vocal : ').lower()
  ingresados.append(vocal)
##ya conozco el contenido total de "ingresados"
for x in ingresados:
  i=0
  for y in vocales:
    if(x==y):
      resumen[i]=resumen[i]+1
    i=i+1
##mostrar resultados:
print('='*25)
for x in range(0,5):
  print(vocales[x], resumen[x], sep='\t')
print('='*25)