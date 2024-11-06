# Importar el diccionario desde archivo1
from Diccionario import diccionario

# Definir la función que retorna las claves del diccionario
def obtener_claves():
    return diccionario.keys()

# Definir la función que retorna el valor asociado a una clave
def obtener_valor_por_clave(clave):
    return diccionario.get(clave)

# Eliminar las claves "Apellido" y "Number" del diccionario
diccionario.pop("Apellido", None)  # Elimina "Apellido"
diccionario.pop("Number", None)    # Elimina "Number"

# Obtener el iterable de pares clave-valor
diccionarioIterable = diccionario.items()

# Imprimir el diccionario actualizado
print(diccionario)  # Imprime {'Nombre': 'Stephano'}

# Imprimir el iterable de pares clave-valor
print(diccionarioIterable)  # Imprime dict_items([('Nombre', 'Stephano')])

# Usar la función para mostrar las claves restantes
claves = obtener_claves()
print(claves)  # Imprime dict_keys(['Nombre'])

# Usar la función para obtener el valor de la clave "Nombre"
valor = obtener_valor_por_clave("Nombre")
print(valor)  # Imprime 'Stephano'
"""# Importar el diccionario desde archivo1
from Diccionario import diccionario

# Definir la función que retorna las claves del diccionario
def obtener_claves():
    return diccionario.keys()

# Definir la función que retorna el valor asociado a una clave
def obtener_valor_por_clave(clave):
    return diccionario.get(clave)

# Eliminar las claves "Apellido" y "Number" del diccionario
diccionario.pop("Apellido", None)  # Elimina "Apellido"
diccionario.pop("Number", None)    # Elimina "Number"

# Obtener el iterable de pares clave-valor
diccionarioIterable = diccionario.items()

# Imprimir el diccionario actualizado
print(diccionario)  # Imprime {'Nombre': 'Stephano'}

# Imprimir el iterable de pares clave-valor
print(diccionarioIterable)  # Imprime dict_items([('Nombre', 'Stephano')])

# Limpiar el diccionario
diccionario.clear()

# Imprimir el diccionario después de limpiarlo
print(diccionario)  # Imprime {}

# Usar la función para mostrar las claves restantes (debería estar vacío)
claves = obtener_claves()
print(claves)  # Imprime dict_keys([])

# Intentar obtener el valor de la clave "Nombre" (debería devolver None)
valor = obtener_valor_por_clave("Nombre")
print(valor)  # Imprime None
"""