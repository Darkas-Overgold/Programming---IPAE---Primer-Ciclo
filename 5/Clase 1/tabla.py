##ejercicio 3
##ingresar 5 numeros mayores de 0
##mostrar tabla de multiplicar del 1 al 12
##solo de  numeros pares
for x in range(1,101):
  n=int(input(f'{x} : Ingrese un numero : '))
  while(n<=0):
    print('Numero ingresado incorrecto 😢')
    n=int(input(f'{x} : Re-ingrese el numero : '))
  if(n%2==0):
    print('='*20)
    print('tabla de multiplicar')
    for i in range(1,13):
      print(f'{n} x {i} = {n*i}')
    print('')