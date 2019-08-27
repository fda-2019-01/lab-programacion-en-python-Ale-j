##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##

# resumen para el resto de puntos
import glob as gl
archivo = gl.glob("data.csv")
datos = open("data.csv", 'rt').readlines()
datos = [line[:-1] for line in datos]
datos = [line.replace("\t", ",") for line in datos]
datos = [line.split(',') for line in datos]
#primero se selecciona sola primer columna y se ordena 
datos2 = [i[2] for i in datos]
datos3 = set(datos2)
#Extraer los meses sinconvertir a fecha
datos4 = sorted([i[5:7] for i in datos2])
#ordenarlos
datos5 = set(datos4)

lista1 = []
for i in datos5:
  p = [i]
  d = 0
  for x in datos4:
    if x == i:
      d = d+1
  p= p+[d]
  lista1 = sorted(lista1+[p])
for ite in lista1:
  res = str(ite[0])+ ","+ str(ite[1])
  print(res)
