# Listas para almacenar datos de empleados
nombres = []
categorias = []
sueldos = []
# Ingresar datos de 5 empleados
for i in range(5):  # Cambia a 100 para el número de empleados
    print(f"\n--- Ingresando datos del empleado {i + 1} ---")
    nombre = input("Ingrese el nombre del empleado: ")
    nombres.append(nombre)
    print("Seleccione la categoría de trabajo:")
    print(" M : Marketing")
    print(" V : Ventas")
    print(" C : Compras")
    while True:
        categoria = input("Ingrese categoría (M, V, C): ").upper()
        if categoria in ['M', 'V', 'C']:
            categorias.append(categoria)
            break
        else:
            print("Categoría inválida. Ingrese 'M', 'V' o 'C'.")
    while True:
        sueldo = float(input("Ingrese sueldo (mínimo 1100): "))
        if sueldo >= 1100:
            sueldos.append(sueldo)
            break
        else:
            print("El sueldo debe ser al menos 1100.")
# Cálculo de cantidad de empleados y promedio de sueldos por categoría
categorias_unicas = ['M', 'V', 'C']
categoria_nombres = {'M': 'Marketing', 'V': 'Ventas', 'C': 'Compras'}
for categoria in categorias_unicas:
    sueldos_categoria = [sueldos[i] for i in range(len(sueldos)) if categorias[i] == categoria]
    if sueldos_categoria:
        cantidad = len(sueldos_categoria)
        promedio = sum(sueldos_categoria) / cantidad
        print(f"\nCategoría: {categoria_nombres[categoria]}")
        print(f"Cantidad de empleados: {cantidad}")
        print(f"Promedio de sueldo: {promedio:.2f}")
    else:
        print(f"\nCategoría: {categoria_nombres[categoria]}")
        print("No hay empleados en esta categoría.")