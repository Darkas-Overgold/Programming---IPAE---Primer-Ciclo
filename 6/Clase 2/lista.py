##ejercicio 6:

import random

lista1=[]
lista2=[]

for x in range(40):
  n1=random.randint(1,100)
  lista1.append(n1)
  n2=random.randint(1,100)
  lista2.append(n2)

#recorrer
lista3=[]
for x in range(40):
  n1=lista1[x]
  n2=lista2[x]
  if((n1%2==0) and (n2%2==0)):
    lista3.append(n1+n2)

#reporte:
lista3.sort()
print(lista1)
print(lista2)
print(lista3)