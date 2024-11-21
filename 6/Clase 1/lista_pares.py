#ingresar 5 numeros por teclado
#almacenarlos en una lista
#mostrar pares e impares

numeros=[]

for x in range(1,6):
  numero=int(input('Ingrese numero : '))
  numeros.append(numero)

print('====================')
print('resultados:')

for numero in numeros:
  if(numero%2==0):
    print(numero, 'es par ✔')
  else:
    print(numero, 'es impar 👀')
print('====================')
