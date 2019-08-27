##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
# resumen para el resto de puntos
import glob as gl
import csv
archivo = gl.glob("data.csv")
datos = open("data.csv", 'r').readlines()
datos = [line[:-1] for line in datos]
datos = [line.replace("\t", ",") for line in datos]
datos = [line.split(',') for line in datos]
datos = [line[5:] for line in datos]
datos = [[row for row in line if len(row)==5] for line in datos]
datos = [[row[0:3] for row in line] for line in datos]
datos2 = []
for line in datos:
  for row in line:
    datos2.append(row)
datos2 = sorted(datos2)
datos3 = set(datos2)
datos3 = [line for line in datos3]
datos3 = sorted(datos3)
lst=[]
for valor in datos3:
  conteo = datas.count(valor)
  war=[valor,conteo]
  lst= lst+[war]

file2 = gl.glob("data1.csv*")
data1 = open("data1.csv", "w")
x = csv.writer(data1, delimiter=",",quoting=csv.QUOTE_NONNUMERIC)
for i in range(len(lst)):
  x.writerow(lst[i])
print(open("data1.csv","r").read())
