##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
## solucion
#primero se selecciona sola primer columna y se ordena
import glob as gl
archivo = gl.glob("data.csv")
data = open("data.csv", 'rt').readlines()
data = [line[:-1] for line in data]
data = [line.replace("\t", ",") for line in data]
data = [line.split(',') for line in data]
data1 = [i[1] for i in data]


data2 = [i[0] for i in data]
data3 = set(data2)
# ahora se procede a contar 

l = []
for i in data3:
  c = 0
  
  for x in data2:
    if i == x:
      c = c + 1
  l.append((i, c))
  l = sorted(l)

for i in l:
  print(i[0]+','+str(i[1]))
  
