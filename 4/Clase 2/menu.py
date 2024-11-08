#Crear un menú para agregar, listar, editar y eliminar elementos de una lista.
# Inicializar una lista vacía para almacenar elementos
elementos = []
while True:
    # Mostrar el menú
    print("="*20)
    print("Menú:" .center(20))
    print("="*20)
    print("1: Ingresar")
    print("2: Listar")
    print("3: Editar")
    print("4: Eliminar")
    print("0: Salir")
    print("="*20)
    # Leer la opción del usuario
    opcion = input("Selecciona una opción: ")
    # Validar que la opción ingresada sea un dígito
    if not opcion.isdigit():
        print("Entrada no válida. Por favor, ingresa un número.")
        continue
    opcion = int(opcion)  # Convertir a entero después de validarlo como dígito
    # Opciones del menú
    if opcion == 1:
        # Ingresar un nuevo elemento
        elemento = input("Ingresa un nuevo elemento: ")
        elementos.append(elemento)
        print(f"'{elemento}' ha sido agregado.")
    elif opcion == 2:
        # Listar todos los elementos
        print("Elementos guardados:")
        for i, item in enumerate(elementos, start=1):
            print(f"{i}. {item}")
    elif opcion == 3:
        # Editar un elemento existente
        if not elementos:
            print("No hay elementos para editar.")
        else:
            indice = input("Ingresa el número del elemento que deseas editar: ")
            if indice.isdigit() and 1 <= int(indice) <= len(elementos):
                nuevo_valor = input("Ingresa el nuevo valor: ")
                elementos[int(indice) - 1] = nuevo_valor
                print("Elemento actualizado.")
            else:
                print("Número de elemento no válido.")
    elif opcion == 4:
        # Eliminar un elemento existente
        if not elementos:
            print("No hay elementos para eliminar.")
        else:
            indice = input("Ingresa el número del elemento que deseas eliminar: ")
            if indice.isdigit() and 1 <= int(indice) <= len(elementos):
                eliminado = elementos.pop(int(indice) - 1)
                print(f"'{eliminado}' ha sido eliminado.")
            else:
                print("Número de elemento no válido.")
    elif opcion == 0:
        # Salir del programa
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")