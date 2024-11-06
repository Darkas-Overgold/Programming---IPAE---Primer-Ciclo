# Abre el archivo en modo lectura con codificación UTF-8
with open("Procesamiento de datos\\test.txt", encoding="UTF-8") as archivo:
# Lee el contenido del archivo
    contenido = archivo.read()
    # Imprime el contenido del archivo
    print(contenido)