pip install bcrypt

#ejercicio 2
#implementar un sistema de matriculas por correo
#1 o mas cursos

cursos={}
cursos["py"]="Programacion en python"
cursos['web']="Programacion para front end"
cursos['bd']="Introduccion a base de datos"
cursos['poo']="Programacion orientado a objetos"
cursos['ive']="Investigacion y etica II"

matricula=[]

#solicitar el correo:

print('='*40)
print('sistema de matriculas'.center(40))
print('='*40)
correo=input('correo institucional : ')

#validar correo

if 'zegel' in correo:

  while True:
    print('='*40)
    print('seleccionar cursos')
    print('='*40)
    print('codigo','\t','curso')
    for curso in cursos:
      print(curso,'\t',cursos[curso])
    print('x','\t','salir del menu')
    print('='*40)
    codigo=input('codigo : ')
    if(codigo=='x'):
      print('fin del programa 😢')
      break
    if(codigo in cursos.keys()):
      #matricula
      matricula.append(codigo)
      print('curso agregado 😊')
    else:
      print('codigo erroneo 😢')

# Diccionario de cursos con sus detalles (cupo máximo y lista de estudiantes)
cursos = {
    1: {"nombre": "Python para Principiantes", "cupo": 2, "estudiantes": []},
    2: {"nombre": "Java Avanzado", "cupo": 3, "estudiantes": []}
}

# Lista de estudiantes registrados en el sistema
estudiantes_registrados = []

# Función para mostrar los cursos disponibles
def mostrar_cursos():
    print("Cursos disponibles:")
    for curso_id, detalles in cursos.items():
        print(f"{curso_id}. {detalles['nombre']} - Cupo: {detalles['cupo']} - Inscritos: {len(detalles['estudiantes'])}")

# Función para registrar un estudiante
def registrar_estudiante(estudiante):
    if estudiante not in estudiantes_registrados:
        estudiantes_registrados.append(estudiante)
        print(f"{estudiante} se ha registrado exitosamente en el sistema.")
    else:
        print(f"{estudiante} ya está registrado en el sistema.")

# Función para matricular a un estudiante en un curso
def matricular_estudiante(estudiante, curso_id):
    if estudiante not in estudiantes_registrados:
        print(f"Error: {estudiante} no está registrado en el sistema.")
        return

    if curso_id not in cursos:
        print("Error: El curso seleccionado no es válido.")
        return

    curso = cursos[curso_id]

    # Verificar si el estudiante ya está inscrito en este curso
    if estudiante in curso["estudiantes"]:
        print(f"{estudiante} ya está inscrito en el curso {curso['nombre']}.")
        return

    # Verificar si el curso tiene espacio
    if len(curso["estudiantes"]) < curso["cupo"]:
        curso["estudiantes"].append(estudiante)
        print(f"{estudiante} se ha inscrito exitosamente en el curso {curso['nombre']}.")
    else:
        print(f"Lo siento, el curso {curso['nombre']} está lleno.")

# Función para mostrar los estudiantes inscritos en un curso
def mostrar_estudiantes(curso_id):
    if curso_id not in cursos:
        print("Error: El curso seleccionado no es válido.")
        return

    curso = cursos[curso_id]
    print(f"Estudiantes inscritos en el curso {curso['nombre']}:")
    for estudiante in curso["estudiantes"]:
        print(f"- {estudiante}")

# Crear un flujo interactivo con el usuario
def menu():
    while True:
        print("\nBienvenido al sistema de matrículas de cursos.")
        print("1. Mostrar cursos disponibles")
        print("2. Registrar estudiante")
        print("3. Matricular estudiante en un curso")
        print("4. Mostrar estudiantes inscritos en un curso")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_cursos()
        elif opcion == "2":
            estudiante = input("Introduce el nombre del estudiante: ")
            registrar_estudiante(estudiante)
        elif opcion == "3":
            estudiante = input("Introduce el nombre del estudiante: ")
            mostrar_cursos()
            curso_id = int(input("Selecciona el número del curso al que te quieres matricular: "))
            matricular_estudiante(estudiante, curso_id)
        elif opcion == "4":
            mostrar_cursos()
            curso_id = int(input("Selecciona el número del curso para ver los estudiantes: "))
            mostrar_estudiantes(curso_id)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

# Ejecutar el menú
menu()