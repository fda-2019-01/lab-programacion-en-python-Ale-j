##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
# resumen para el resto de puntos
import glob as gl
archivo = gl.glob("data.csv")
datos = open("data.csv", 'r').readlines()
datos = [line[:-1] for line in datos]
datos = [line.replace("\t", ",") for line in datos]
datos = [line.split(',') for line in datos]
alpha = [line[0] for line in datos]
variable = [line[5:] for line in datos]
variable = [[fila for fila in line if len(fila)==5] for line in variable]
varibale = [[int(fila[4]) for fila in line] for line in variable]
arab = []
for fila in variable:
  a=0
  for num in row:
    a = a+num
  arab.append(a)
arab
for i in range(len(arab)):
  solucion = str(alpha[i])+","+str(arab[i])
  print(solucion)
