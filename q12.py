##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
# resumen para el resto de puntos
import glob as gl
archivo = gl.glob("data.csv")
datos = open("data.csv", 'r').readlines()
datos = [line[:-1] for line in datos]
datos = [line.replace("\t", ",") for line in datos]
datos = [line.split(',') for line in datos]
datos2 = [[fila for fila in line if len(fila) == 1] for line in datos]
datos2 = [line[1:] for line in datos2]
datos3 = [line[2:] for line in datos2]
lst = []
for valores in datos3:
  for vaina in valores:
    lst = lst+[vaina]
lst = set(lst)
lst = list(lst)
lst = sorted(lst)
respuesta = []
for alpha in lst:
  num = [alpha]
  contador = 0
  for fila in datos2:
    if alpha in fila:
      contador = contador + int(fila[0])
  num = num + [contador]
  respuesta = respuesta + [num]
for line in respuesta:
  final = line[0]+","+str(line[1])
  print(final) 
