sueldo = float(input("Ingrese su sueldo: "))
departamento = input("Ingrese su departamento (A, B, C o D): ").upper()
years = int(input("Ingrese sus años de experiencia: "))
def calcular_sueldo(departamento, sueldo, years):
    sueldo = 0
    if departamento == 'A':
        if 2 <= years <= 5:
            sueldo *= 1.2
    elif departamento == 'B':
        if 5 <= years:
            sueldo *= 1.3
    elif departamento == 'C':
        if years < 2:
            sueldo *= 1.05
    elif departamento == 'D':
        sueldo *= 0.75
    return sueldo
sueldo_final = calcular_sueldo(departamento, sueldo, years)
print(f"Su sueldo ajustado es: {sueldo_final:.2f}")