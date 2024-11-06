def sumar():
    while True:
        a = input("Número 1: ")
        b = input("Número 2: ")
        try: 
            resultado = int(a) +  int (b)
            break
        except:
            print("Te solicité un número, tonoto. No seas gracioso.")
        else:
            break
        finally:
            print("Manejo de excepción finalizado:")
    return resultado
print(sumar())