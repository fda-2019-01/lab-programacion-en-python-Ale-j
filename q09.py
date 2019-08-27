##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas y sin repetir letra) 
## de la primera  columna que aparecen asociadas a dicho valor de la 
## segunda columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'B', 'D', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
# resumen para el resto de puntos
import glob as gl
archivo = gl.glob("data.csv")
datos = open("data.csv", 'rt').readlines()
datos = [line[:-1] for line in datos]
datos = [line.replace("\t", ",") for line in datos]
datos = [line.split(',') for line in datos]
datos = sorted([[line[1], line[0]] for line in datos])
datos2 = set([line[0] for line in datos])
uno = []
for num in datos2:
  x = [num]
  y = []
  
  for ind in datos:
    
    if num == ind[0]:
      y.append(ind[1])
  y = set(y)
  for line in y:
    x = sorted(x+[line])
  uno = uno+[x]
uno = sorted(uno)
for row in uno:
  dos = row[1:]
  tres=(row[0],dos)
  print(tres)
