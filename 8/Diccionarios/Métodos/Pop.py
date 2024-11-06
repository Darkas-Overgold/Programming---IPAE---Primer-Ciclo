# Importar el diccionario desde Diccionario
from Diccionario import diccionario
# Eliminando un elemento del diccionario
diccionario.pop("Apellido", None)  # Elimina "Apellido"
diccionario.pop("Number", None)    # Elimina "Number"
print(diccionario)