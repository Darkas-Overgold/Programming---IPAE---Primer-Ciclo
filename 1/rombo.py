altura = int(input("Ingresa la altura del rombo (parte superior): "))
# Parte superior del rombo
for i in range(1, altura + 1):
    print(' ' * (altura - i) + '*' * (2 * i - 1))
# Parte inferior del rombo
for i in range(altura - 1, 0, -1):
    print(' ' * (altura - i) + '*' * (2 * i - 1))
