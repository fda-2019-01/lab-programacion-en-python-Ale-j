##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras de la primera columna que aparecen
## asociadas a dicho valor de la segunda columna. Esto es:
##
##    ('0', ['C'])
##    ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##    ('2', ['A', 'E', 'D'])
##    ('3', ['A', 'B', 'D', 'E', 'E'])
##    ('4', ['E', 'B'])
##    ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##    ('6', ['C', 'E', 'A', 'B'])
##    ('7', ['A', 'C', 'E', 'D'])
##    ('8', ['E', 'E', 'A', 'B'])
##    ('9', ['A', 'B', 'E', 'C'])
##
##
# resumen para el resto de puntos
import glob as gl
archivo = gl.glob("data.csv")
datos = open("data.csv", 'rt').readlines()
datos = [line[:-1] for line in datos]
datos = [line.replace("\t", ",") for line in datos]
datos = [line.split(',') for line in datos]
datos = [[line[1], line[0]] for line in datos]
datos2 = set([line[0] for line in datos])
list1 = []
for num in datos2:
  var = [num]
  for val in datos:
    if num == val[0]:
      var.append(val[1])
  var = [y for y in var]
  list1 = list1+[var]
list2 = [line[0] for line in list1]
list3 = [line[1:] for line in list1]
var2=[]
for i in range(0, len(list1)):
  var3= (list2[i], list3[i])
  var2 = var2+[var3]
var2 = sorted(var2)
for line in var2:
  print(line) 
