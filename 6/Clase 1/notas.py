import random
#ejercicio 2
#lista con 20 notas de N1
#lista con 20 notas de N2

n1=[]
n2=[]
p=[]

for x in range(20):
  a=random.randint(0,20)
  n1.append(a)
  b=random.randint(0,20)
  n2.append(b)

  c=(a+b)/2
  p.append(c)

ca=0
cd=0

for x in p:
  if(x>10.5):
    ca=ca+1
    print(x,'aprobado')
  else:
    cd=cd+1
    print(x,'des aprobado')

print('==============')
print('aprobados :',ca)
print('desaprobados :',cd)