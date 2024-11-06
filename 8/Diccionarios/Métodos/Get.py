# Importar el diccionario desde Diccionario
from Diccionario import diccionario
# Definir la función que obtiene el valor usando el método get
def obtenerValorPorClave(clave):
    return diccionario.get(clave, "Clave no encontrada")
# Usar la función para obtener el valor asociado a la clave "Number"
valor = obtenerValorPorClave("Nombre")
valor1 = obtenerValorPorClave("Apellido")
valor2 = obtenerValorPorClave("Number")
print(valor)
print(valor1)
print(valor2)