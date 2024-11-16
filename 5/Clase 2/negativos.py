#b) Desarrolle un algoritmo que permita ingresar 15 números negativos, luego
#indicar la suma de los que fueron mayores a -10.
import random as rnd
s=0
print('======================')
for x in range(15):
  n=rnd.randint(-100,0)
  if(n>-10):
    s=s+n
    print(x,n,'👍🏽',sep='\t')
  else:
    print(x,n,sep='\t')
print('======================')
print(' resultados:')
print('======================')
print('suma : ', s)