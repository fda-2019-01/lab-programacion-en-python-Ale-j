##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
# resumen para el resto de puntos
import glob as gl
archivo = gl.glob("data.csv")
datos = open("data.csv", 'rt').readlines()
datos = [line[:-1] for line in datos]
datos = [line.replace("\t", ",") for line in datos]
datos = [line.split(',') for line in datos]
#primero se seleccionan las 2 primeros registros y se ordenan
datos2 = sorted([[line[0], line[1]] for line in datos])
#seleciona primer registro
datos3 = [line[0] for line in datos2]
datos3 = set(datos3)
# se genera lal lista y variables
lista1 = []
for reg1 in datos3:
  lista2 = []
  for x in datos2:
    if reg1 == x[0]:
      lista2 = lista2+[x[1]]
  objeto = [reg1, max(lista2), min(lista2)]
  lista1=lista1+[objeto]
lista1 = sorted(lista1)
for valor in lista1:
  result= valor[0]+","+str(valor[1])+","+str(valor[2])
  print(result)
