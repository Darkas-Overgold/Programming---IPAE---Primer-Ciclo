# Número de niveles de la pirámide (incluyendo el punto más alto)
altura = 5

# Parte creciente de la pirámide
for i in range(1, altura + 1):
    print(' ' * (altura - i) + '*' * i)

# Parte decreciente de la pirámide
for i in range(altura - 1, 0, -1):
    print(' ' * (altura - i) + '*' * i)