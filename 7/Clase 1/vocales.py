#hallar la cantidad de vocales de una palabra usando funciones
def nvocales(texto):
  vocales=['a','e','i','o','u']
  n=0
  for c in texto:
    if(c in vocales):
      n=n+1
  return n
nvocales('hello')