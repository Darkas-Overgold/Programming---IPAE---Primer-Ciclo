import random
numeros = [random.randint(10,99) for _ in range(50)]
print("Lista de números generados:", numeros)
while True:
  numero_usuario = (input("Digite un número dentro del intervalo 10-99."))
  if numero_usuario.isdigit():
    numero_usuario = int(numero_usuario)
    if 10<= numero_usuario <= 99:
      break
    else:
      print("Elemento fuera del intervalo.")
  else:
    print("Digita un número válido.")
#Resultado
contador = 0
for numero in numeros:
  if numero == numero_usuario:
    contador += 1
if contador>0:
  print(f"El número {numero_usuario} se repite {contador} veces.")
else:
  print(f"El número {numero_usuario} no se encontró en la lista.")

v=[ "a" for x in range(5)]
v

for x in range(5):
  print("a")