class MyException(Exception):
    def __init__(self,err):
        print(f"Cometiste el siguiente error: {err}")
# Lanzando una excepción
raise MyException("Sticking out your gyatt for the rizzler")
# Manejando mi propia excepción.
try:
    raise MyException("Sticking out your gyatt for the rizzler")
except:
    print("Un error lo comete cualquiera.")