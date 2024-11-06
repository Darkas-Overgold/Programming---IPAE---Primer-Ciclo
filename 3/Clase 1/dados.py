import random
def lanzar_dados():
  return random.randint(1, 6), random.randint(1, 6)
def condiciones_ganadoras(dado1, dado2):
  # condicion ganadora: al menos un dado muestra 6
  if dado1 == 5 and dado2 == 5 or dado1 == 5 and dado2== 6:
      return True, "Ganaste al menos un dado 6"
  #condicion ganadora: ambos dados son iguales (par)
  if dado1 == dado2:
    return True, "Ganaste obtienes un par"
    return False, "no hay condiciones ganadoras"
def main():
  dado1, dado2 = lanzar_dados()
  print(f"Lanzaste: {dado1} y {dado2}")
  ganador, mensaje = condiciones_ganadoras(dado1, dado2)
  print(mensaje)
if __name__ == "__main__":
  main()
# d1=int(input('Ingrese dado 1: '))
# d2=int(input('Ingrese dado 2: '))
import random
d1=random.randint(1,6)
d2=random.randint(1,6)
print('dado 1: ', d1)
print('dado 2: ', d2)
print('='*20)
if(d1==5 and d2==5):
  print('Ganaste xD')
elif(d1==6 and d2==6):
  print('Ganaste xD')
else:
  print('No ganaste :(')
# d1=int(input('Ingrese dado 1: '))
# d2=int(input('Ingrese dado 2: '))
import random
d1=random.randint(1,6)
d2=random.randint(1,6)
print('dado 1: ', d1)
print('dado 2: ', d2)
print('='*20)
mensaje='No ganaste'
if((d1==5 and d2==5) or (d1==6 and d2==6)):
  mensaje='si ganaste'
if((d1==1 and d2==1) or (d1==2 and d2==2)):
  mensaje='Sí ganaste'
print(mensaje)