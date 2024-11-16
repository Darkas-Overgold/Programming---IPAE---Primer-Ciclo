##propuesto A
##Se ingresan 50 números que representan a un mes del año (validar que
##estén entre 1 y 12), luego indicar cuántos de esos números representaron
##a otoño o verano.
import random as rnd
nv=0
no=0
ni=0
np=0
for x in range(1,51):
  mes=rnd.randint(0,100)
  print('Mes : ', mes)
  if(mes<=0 or mes>12):
    print('Mes incorrecto 😢')
  else:
    print('Mes correcto 👍🏽')

  if(mes in [1,2,3]):
    ##verano!
    nv=nv+1
  if(mes in [4,5,6]):
    ##otoño!
    no=no+1
  if(mes in [7,8,9]):
    ##invierno!
    ni=ni+1
  if(mes in [10,11,12]):
    ##primavera!
    np=np+1
##mostrar resultados!:)
print()
print(' resultados!')
print('============================')
print('verano : ', nv)
print('otoño : ', no)
print('invierno : ', ni)
print('primavera : ', np)
print('============================')