while True:
    mes = input("Digita el número del mes (1-12): ")
    # Verificar si la entrada es un número y está en el rango válido
    if mes.isdigit() and 1 <= int(mes) <= 12:
        print(f"Número de mes válido: {mes}")
        break
    else:
        print("Entrada no válida. Por favor, digita un número entre 1 y 12.")