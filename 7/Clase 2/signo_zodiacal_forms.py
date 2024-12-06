import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

# Función para determinar el signo zodiacal
def obtener_signo_zodiacal(fecha):
    dia = fecha.day
    mes = fecha.month
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricornio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Piscis"

# Función para manejar la selección de fecha
def mostrar_signo():
    fecha_seleccionada = calendario.get_date()
    fecha = datetime.strptime(fecha_seleccionada, "%m/%d/%y")
    signo = obtener_signo_zodiacal(fecha)
    resultado.set(f"Tu signo zodiacal es: {signo}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Signo Zodiacal")

# Etiqueta de instrucciones
ttk.Label(ventana, text="Selecciona tu fecha de nacimiento:", font=("Arial", 12)).pack(pady=10)

# Calendario para seleccionar la fecha
calendario = Calendar(ventana, selectmode="day", year=2000, month=1, day=1)
calendario.pack(pady=10)

# Botón para calcular el signo zodiacal
boton = ttk.Button(ventana, text="Calcular Signo Zodiacal", command=mostrar_signo)
boton.pack(pady=10)

# Etiqueta para mostrar el resultado
resultado = tk.StringVar()
ttk.Label(ventana, textvariable=resultado, font=("Arial", 12)).pack(pady=10)

# Mantener la ventana abierta
ventana.mainloop()
