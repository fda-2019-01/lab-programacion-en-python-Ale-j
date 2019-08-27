##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
# resumen para el resto de puntos
import glob as gl
import csv
archivo = gl.glob("data.csv")
datos = open("data.csv", 'r').readlines()
datos = [line[:-1] for line in datos]
datos = [line.replace("\t", ",") for line in datos]
datos = [line.split(',') for line in datos]
datos2 = [line[0] for line in datos]
datos = [line[3:] for line in datos]
datos2_1 = [[fila for fila in line if len(fila) == 1] for line in datos]
datos2_2 = [[fila for fila in line if len(fila) == 5] for line in datos]
datos2_3 = [[datos2[i], len(datos2_1[i]), len(datos2_2[i])] for i in range(len(datos))]

doc = gl.glob("respuesta.csv")
docs = open("respuesta.csv", "w")
writer = csv.writer(docs, delimiter = ",", quoting = csv.QUOTE_NONNUMERIC) 
for i in range(len(datos2_3)):
  writer.writerow(datos2_3[i])
print(open("respuesta.csv", "r").read())
