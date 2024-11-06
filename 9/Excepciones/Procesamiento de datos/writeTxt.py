#Sobreescribir:
"""with open('Procesamiento de datos\\test.txt','w',encoding="UTF-8") as archivo:
    archivo.writelines(["Hola causa\n","Gaaaa"])"""
with open('Procesamiento de datos\\test.txt','a',encoding="UTF-8") as archivo:
    archivo.write("\n")
    for i in range (5):
        archivo.write(f"Línea {i+1} agregada\n")