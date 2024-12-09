from getpass import getpass

# Diccionario de usuarios con contraseñas
usuarios = {
    "pedro@gmail.com": "123",
    "maria@hotmail.com": "123",
    "jose@yahoo.es": "123"
}

# Mostrar el diccionario de usuarios con contraseñas como asteriscos
def mostrar_usuarios_con_asteriscos(usuarios):
    print("Usuarios registrados:")
    for usuario, contrasena in usuarios.items():
        print(f"{usuario}: {'*' * len(contrasena)}")
    print("=" * 20)

# Verificar credenciales de login
def verificar_login(correo, contrasena):
    return usuarios.get(correo) == contrasena

# Función principal de login
def login():
    print("=" * 20)
    print("LOGIN".center(20))
    print("=" * 20)

    correo = input("Correo: ")
    contrasena = getpass("Password: ")  # Oculta la entrada de la contraseña en la terminal

    if correo in usuarios.keys():
        if verificar_login(correo, contrasena):
            print("¡Bienvenido 😊!")
        else:
            print("Password incorrecto 😢")
    else:
        print("Usuario no existe 😢")

# Mostrar usuarios y ejecutar login
mostrar_usuarios_con_asteriscos(usuarios)
login()
