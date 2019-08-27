##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas) de la primera 
## columna que aparecen asociadas a dicho valor de la segunda 
## columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'A', 'B', 'D', 'E', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E', 'E'])
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
lista1 = []
for n in datos2:
  var = [n]
  for val in datos:
    if n == val[0]:
      var.append(val[1])
  var = [y for y in var]
  lista1 = lista1+[var]
var2 = [line[0] for line in lista1]
cinco = [line[1:] for line in lista1]
var1=[]
for i in range(0, len(lista1)):
  var3= (var2[i], cinco[i])
  var1 = var1+[var3]
var1 = sorted(var1)
for line in var1:
  print(line) 
