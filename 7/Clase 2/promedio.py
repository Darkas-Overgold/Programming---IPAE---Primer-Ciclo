import random

def promedio(lista):
  p=sum(lista)/len(lista)
  return p

lista=[random.randint(-50,50) for x in range(100)  ]


positivos=[x for x in lista if x>0 ]
negativos=[x for x in lista if x<0 ]

print(lista)
print(positivos)
print(negativos)

print('=========================')
print(promedio(positivos))
print(promedio(negativos))