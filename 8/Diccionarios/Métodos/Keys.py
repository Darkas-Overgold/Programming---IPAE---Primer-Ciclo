#from Diccionario import Diccionario
# Importar el diccionario desde archivo1
from Diccionario import diccionario
# Definir la función que retorna las claves del diccionario
def obtenerClaves():
    return diccionario.keys()
# Usar la función y mostrar las clavaes
claves = obtenerClaves()
print(claves)