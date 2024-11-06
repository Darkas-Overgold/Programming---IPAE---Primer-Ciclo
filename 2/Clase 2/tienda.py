costo_producto = 0
tipo_cliente = input("Ingrese el tipo de cliente (A, B o C): ").upper()
costo_producto = float(input("Ingrese el costo del producto: "))
cantidad_compras = int(input("Ingrese la cantidad de veces que ha comprado: "))
if tipo_cliente == 'A' and cantidad_compras > 5:
    costo_producto *= 0.7
elif tipo_cliente == 'B' and cantidad_compras > 6:
    costo_producto *= 0.8
elif tipo_cliente == 'B' and cantidad_compras < 2:
    costo_producto *= 0.95
elif tipo_cliente == 'C' and cantidad_compras > 4:
    costo_producto *= 0.75
print(f"El costo final del producto es: {costo_producto:.2f}")