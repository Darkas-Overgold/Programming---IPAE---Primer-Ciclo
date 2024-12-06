#diccionarios
v={}
v['zegel']='instituto de educacion superior'
v['zenegal']='pais del occidente'
v['zenteno']='apellido'
#actualizar
v['zegel']='escuela de educacion superior'
#eliminar zenteno
del v['zenteno']
#listar
for x in v:
  print(x,'\t',v[x])
v['zorro']='mamifero ...'
v[9]='nueve'
v[10]=1662
v # Invocación del diccionario