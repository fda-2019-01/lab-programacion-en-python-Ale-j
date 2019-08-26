##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
## Soluciión al punto
# resumen para el resto de puntos
import glob as gl
archivo = gl.glob("data.csv")
datos = open("data.csv", 'rt').readlines()
datos = [line[:-1] for line in datos]
datos = [line.replace("\t", ",") for line in datos]
datos = [line.split(',') for line in datos]
datos3 = [i[0] for i in datos]
datos3 = sorted(datos3)
d = [i[1] for i in datos]
d = [int(i) for i in d]
res = dict.fromkeys(datos3, 0)
for a, b in zip(datos3, d):
   res[a] += b

print(*(f"{key}, {value}" for key, value in res.items()), sep="\n")


