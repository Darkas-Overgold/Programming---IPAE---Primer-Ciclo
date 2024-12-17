#calculo de IMC

p=float(input('Ingrese peso (kg) : '))
h=float(input('Ingrese altura (m) : '))

try:
  imc=p/(h*h)
  print('IMC : ', imc)
except:
  print('parametros incorrectos 😢')

# Función para calcular el IMC
def calcular_imc(peso, altura):
    # Fórmula del IMC
    imc = peso / (altura ** 2)
    return imc

# Función para interpretar el IMC
def interpretar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Solicitar al usuario el peso y la altura
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

# Calcular el IMC
imc = calcular_imc(peso, altura)

# Mostrar el resultado
print(f"Tu IMC es: {imc:.2f}")
print(f"Interpretación: {interpretar_imc(imc)}")