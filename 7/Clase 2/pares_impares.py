#propuesto C
import random
# numeros=[random.randint(0,100) for x in range(100)]

def promedio(numeros):
  p=sum(numeros)/len(numeros)
  return p

def separar(numeros):
  pares=[]
  impares=[]
  for x in numeros:
    if(x%2==0):
      #par
      pares.append(x)
    else:
      impares.append(x)
  return pares, impares

numeros=[]
for x in range(100):
  numeros.append(random.randint(0,100))

pares, impares=separar(numeros)

print('0'*40)
print(numeros)
print(pares)
print(impares)
print('0'*40)
print(promedio(pares))
print(promedio(impares))