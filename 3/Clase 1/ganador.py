#detectar condicion ganadora de 2 dados
#si los numeros son iguales, 1y1 2y2 ... 6y6
#bonus 😊: suma de digitos es 4 (3y1)
import random
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f"Dado 1: {dado1}, Dado 2: {dado2}")
    return dado1, dado2
def es_ganador(dado1, dado2):
    # Condición de números iguales
    if dado1 == dado2:
        return "¡Ganaste! Ambos dados son iguales."
    # Condición de suma de dígitos igual a 4
    elif dado1 + dado2 == 4:
        return "¡Ganaste! La suma de los dados es 4. 😊"
    else:
        return "Lo siento, no ganaste esta vez."
# Lanzar los dados y verificar si hay una condición ganadora
dado1, dado2 = lanzar_dados()
resultado = es_ganador(dado1, dado2)
print(resultado)